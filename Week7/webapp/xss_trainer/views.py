"""
Very simple Flask App.  For Testing
"""

import urllib.parse

import flask

from xss_trainer.meta import app
from xss_trainer.meta import redis_client

# My Selenium Driver

import xss_trainer.levels.baseLevels as baseLevels
import xss_trainer.levels.contrib as contrib
import xss_trainer.levels.intermediate as intermediate

import xss_trainer.webdriver


# Create the Driver
driver = xss_trainer.webdriver.SelenoidDriver()

#Last Request
lastRequest = {}

LEVELS = [baseLevels.Training(),
          baseLevels.NoFilter(),
          baseLevels.ClientFilter(),
          baseLevels.SimpleReplace(),
          baseLevels.BasicRegexp(),
          baseLevels.BasicPHPRegexp(),
          baseLevels.ScriptTagFilter(),
          contrib.EscapeChars(),
          contrib.Encoding(),
          baseLevels.TagAttributes(),
          baseLevels.BootstrapTags(),
          baseLevels.MarkdownOutput(),
          intermediate.SessionTest()]


MAX_LEVEL = len(LEVELS)



@app.route('/')
def main():
    """
    Render the homepage
    """
    #flask.session["bleh"] = b"Bleh"
    if "level" not in flask.session:
        flask.session["level"] = 0

    return flask.render_template('index.html',
                                 level=None,
                                 maxlevel = MAX_LEVEL,
                                 navLevels = LEVELS)

@app.route("/reset")
def reset():
    """
    Clear the Session
    """
    flask.session.clear()
    return flask.redirect(flask.url_for("main"))


@app.route("/konami")
def konami():
    """
    Boost level to 100 for testing
    """
    flask.session["level"] = 100
    return flask.redirect(flask.url_for("main"))


@app.route("/training")
@app.route("/training/<levelId>")
def training(levelId=1):
    """
    Training Levels (Not used at the moment)
    """
    return "Not Yet Implemented {0}".format(levelId)


@app.route("/level")
@app.route("/level/<int:levelId>", methods=["GET","POST"])
def levels(levelId=0):
    """
    Main Driver for the Levels

    @param levelId:  Numeric Id for the Level (from the LEVELS list)
    """

    #First check we are not beyond our level
    userLevel = int(flask.session.get("level"))

    app.logger.info("Request made Level ID %s User Level is %s", levelId, userLevel)
    if levelId >= MAX_LEVEL:
        flask.abort(404)

    if levelId > userLevel:
        #TODO add a page for this
        flask.abort(403)


    submitted = False
    result = False
    payload = None
    message = None
    filtered = None

    #Next we need to get the level itself
    thisLevel = LEVELS[levelId]
    app.logger.debug("Show Level {0}".format(thisLevel))

    #Get the Payload
    payload = thisLevel.getPayload()
    app.logger.debug("Payload is {0}".format(payload))

    if payload:
        submitted = True

        #Perform Filtering
        filtered = thisLevel.sanitise(payload)

        app.logger.debug("FILTERED %s",filtered)
        #Check for XSS

        result = _checkPayload(filtered)

        #Generic Success Message
        if result:
            app.logger.debug("Success")
            if hasattr(thisLevel, "flag"):
                message = "Success! Have a flag: {0}".format(thisLevel.flag)
            else:
                message = "Success! You triggered an alert"

            #Now do something sensible with incrementing the level Id
            #Only increase if we are at the final level
            if levelId == userLevel:
                app.logger.debug("Increment Level")
                flask.session['level'] = userLevel+1

        else:
            message = "You didn't trigger an alert, try again"


    if hasattr(thisLevel, "cookie"):
        cookieKey, cookieValue = thisLevel.cookie
        testCookie = flask.request.cookies.get(cookieKey)
        if testCookie == cookieValue:
            app.logger.debug("Correct Cookie Set")
            if levelId == userLevel:
                app.logger.debug("Increment Level")
                flask.session['level'] = userLevel+1
                    
    

    #Work out the template
    theTemplate = "levels/{0}".format(thisLevel.template)
    return flask.render_template(theTemplate,
                                 level=levelId,
                                 submitted = submitted,
                                 result = result,
                                 message = message,
                                 payload = filtered,
                                 maxlevel = MAX_LEVEL,
                                 navLevels = LEVELS,
                                 thisLevel = thisLevel)


def _checkPayload(payload, level):
    """ Helper Method to check if a payload has triggered the input

    @param payload:  Whatever the user has input
    @param level:  The level the user has submitted
    @return: True if XSS is found
    """

    userIP = flask.request.remote_addr

    redis_client.set("{0}_P".format(userIP),payload)
    redis_client.set("{0}_L".format(userIP), level)
    qString = urllib.parse.urlencode({"ip": userIP})
    theURL = "http://flask:5000/render?{0}".format(qString)
    result = driver.checkPage(theURL)
    app.logger.debug("Result %s", result)
    return result


@app.route("/render")
def render():
    """
    Render a payload specified by a user

    This view will render whatever the user has last submitted
    Making it available for the Selenium instance to check for XSS
    """
    #Get the payload
    theIp= flask.request.args.get("ip",None)

    app.logger.debug("Render For %s", theIp)
    #Fetch the payload from Redis
    try:
        thePayload = redis_client.get("{0}_P".format(theIp))
        theLevel = redis_client.get("{0}_L".format(theIp))
        app.logger.debug("Render Payload: %s", thePayload)
        app.logger.debug("Render Level: %s", theLevel)

    except NameError:
        app.logger.warning("Attempt to get non existant IP")
        thePayload = None



    # Now we can so things with cookies or other page things
    thisLevel = LEVELS[int(theLevel)]
    app.logger.warning("This Level is {0}".format(thisLevel))

    # Check if we give a custom Render Template
    renderTemplate = "render.html"
    if hasattr(thisLevel, "renderer"):
        renderTemplate = thisLevel.renderer


    #Build our Response
    rendered = flask.render_template(renderTemplate,
                                     payload = thePayload.decode())


    response = flask.make_response(rendered)

    if hasattr(thisLevel, "cookie"):
        key, value = thisLevel.cookie
        response.set_cookie(key, value)

    return response


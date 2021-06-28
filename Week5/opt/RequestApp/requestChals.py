"""
Request Based Challenges
"""

import json

import flask
from .meta import app

import logging

import time
import random


#Store the data
automateData = {"time":None,
                "q1": None,
                "q2": None}

@app.route("/challenges/setUA", methods=["GET","POST"])
def userAgentChallenge():

    UA = flask.request.headers.get("user-agent")


    theFlag = False
    if flask.request.method == "POST":
        if UA == "l33t Hax0r":
            theFlag = "245CT{Ch@nging_UA}"
    


    return flask.render_template("userAgentChal.html",
                                 flag = theFlag)

    

@app.route("/challenges/Response")
def responseChallenge():
    return flask.render_template("responseTarget.html")

@app.route("/challenge/theResponse")
def responsePage():
    return flask.render_template("responseChallenge.html")



@app.route("/challenge/automate")
def automateChallenge():

    submitted = False
    flag = False
    if flask.request.args.get("q1"):
        #Something has been sbmitted"
        
        submitted = "Too Slow"
        sTime = time.time()
        u1 = flask.request.args.get("q1")
        u2 = flask.request.args.get("q2")

        if u1 == str(automateData["q1"]):
            if u2 == automateData["q2"]:
                tDelta = sTime - automateData["time"]
                if tDelta < 2:
                    flag = "245{Automation_R0cks}"
                else:
                    submitted = "Too Slow"
            else:
                submitted = "Incorrect"
        else:
            submitted = "Incorrect"
        
        
        
    if not flag:
        logging.warning("Generate New Questions")
        #Work out the Questions
        p1 = random.randrange(10)
        p2 = random.randrange(10)
        q1 = "{0} + {1}".format(p1, p2)
        q1a = p1 + p2

        q2 = random.choice(["Lion El'Jonson",
                           "Fulgrim",
                           "Perturabo",
                           "Jaghatai Khan",
                           "Leman Russ",
                           "Rogal Dorn",
                           "Konrad Curze",
                           "Sanguinius", 
                           "Ferrus Manus",
                           "Angron",
                           "Roboute Guilliman",
                           "Mortarion",
                           "Magnus the Red",
                           "Horus",
                           "Lorgar",
                           "Vulkan",
                           "Corax",
                            "Alpharius Omegon"])

        automateData["time"] = time.time()
        automateData["q1"] = str(q1a)
        automateData["q2"] = q2
        

    return flask.render_template("automateChallenge.html",
                                 q1 = q1,
                                 q2 = q2,
                                 submitted = submitted,
                                 flag = flag)


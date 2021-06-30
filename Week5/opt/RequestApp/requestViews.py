"""
Views for Demoing Requests
"""

import json

import flask
from .meta import app


HTTP_METHODS = ['GET', 'HEAD', 'POST', 'PUT',
                'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']


@app.route("/headers/viewHeaders", methods=HTTP_METHODS)
def requestHeaders():
    """
    Just view any Request Headers (in text)
    """
    return flask.render_template('requestBrowser.html')


@app.route("/headers/getHeaders")
def getHeaders():
    """
    Show the Headers associated with a Get Request
    """
    return flask.render_template('requestBrowserForm.html', method="GET")


@app.route("/headers/postRequest", methods=["GET", "POST"])
def postHeaders():
    """
    Show the Headers associated with a POST Request
    """
    return flask.render_template('requestBrowserForm.html', method="POST")


# @app.route("/headers/requestJson", methods=HTTP_METHODS)
# def requestJson():
#     """
#     View the Request headers in JSON format
#     """

#     logging.warning(flask.request.headers)
#     output = {"method": flask.request.method,
#               "headers": dict(flask.request.headers),
#               "args": dict(flask.request.args),
#               "body": dict(flask.request.form)}
#     response = app.response_class(
#         response=json.dumps(output),
#         status=200,
#         mimetype='application/json'
#     )
#     #What we want is the same information
#     return response


# @app.route("challenges/requests/EM")
# def challenge_requests_email_to_text():
#     """
#     Can we change email to text
#     """
#     pass

# @app.route("challenges/requests/FA")
# def challenge_requests_form_admin():
#     """
#     Can we turn Admin mode on
#     """
#     pass


# @app.route("challenges/requests/UA")
# def challenge_request_useragent():
#     """
#     Can we modify the user agent
#     """
#     pass


# @app.route("challenges/requests/DATTYP")
# def challenge_request_accept():
#     """
#     Can we change the datatype of the response
#     """
#     pass

# @app.route("challenges/requests/HO")
# def challenge_requests_host():
#     """
#     Can we change who the request comes from
#     """
#     pass


# @app.route("challenges/requests/Automate")
# def challenge_requests_automate():
#     """
#     Can we make automated requests
#     """
#     pass

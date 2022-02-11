"""
Very simple Flask App.  For Testing
"""


import json

import flask
from .meta import app
#app = flask.Flask(__name__)

HTTP_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']

import logging

@app.route('/')
def main():
    #payload = flask.request.args.get("payload")
    return flask.render_template('index.html')




@app.route("/admin")
def admin():
    return flask.render_template('admin.html')


@app.route("/my")
@app.route("/my/admin/")

def enum():
    return flask.render_template('enum.html')


@app.route("/my-sql")
def badEnum():
    flask.abort(403)
    return "foo"

@app.route("/my-sql/admin")
@app.route("/my/admin/spider")
def enumSuccess():

    #Can i get the route
#    flask.request.route
    
    return flask.render_template('enum.html',
                                 success=True)
    

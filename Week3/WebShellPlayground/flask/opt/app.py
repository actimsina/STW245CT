"""
Very simple Flask App.  For Testing
"""

import flask
app = flask.Flask(__name__)

import subprocess

@app.route('/')
def main():

    #payload = flask.request.args.get("payload")
    return flask.render_template('index.html')

@app.route("/subprocess")
def subproc():

    command = flask.request.args.get("payload")
    if command:
        output = subprocess.check_output(command, shell=True)
        output = output.decode()
    else:
        output = None
        
    return flask.render_template('subprocess.html', command = command, output = output)

        

@app.route("/eval")
def evalRCE():
    error = None
    output = None
    command = flask.request.args.get("payload")
    if command:
        try:
            output = eval(command)
        except Exception as ex:
            error = ex
        
    return flask.render_template('evalRce.html', command = command, output = output, error=error)

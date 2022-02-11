"""
Metaclasses for level objects

This module contains all the shared functionality for levels
Defining the base class that levels inherit from and any helper functions
"""

import subprocess

import flask

def evalPhp(theCommands):
    """
    Evaluate a PHP command

    @param theCommands:  List of commands to evaluate
    @return: Output of PHP
    """

    with open("/tmp/script.php","w") as fd:
        fd.write("<?php\n")
        for item in theCommands:
            fd.write("{0};\n".format(item))
        fd.write("?>")

    out = subprocess.check_output(["php", "/tmp/script.php"])
    return out



class BaseLevel:
    """
    Base class for levels

    We could define the attributes in an __init__() function,
    but as we are only ever going to have one instance of the subclasses
    we will define indiviually in them.  Therefore we skip the __init__ function
    """
    #def __init__(self):
    #    self.levelname = "Template"
    #    self.template = "levelTemplate.html"

    def getPayload(self):
        """
        Generic Function to get either get or post payloads.

        We can overload this if necessary.

        @return:  Request parameters or data.
        """
        if flask.request.method == "POST":
            payload = flask.request.form.get("payload", None)
        else:
            payload = flask.request.args.get("payload", None)

        return payload


    def sanitise(self, data):
        """
        Filter bad things from user input.

        We call it sanitise as filter is reserved.

        @param data:  User Supplied data
        @return filtered version of the data
        """
        return data

    def __str__(self):
        return self.levelname

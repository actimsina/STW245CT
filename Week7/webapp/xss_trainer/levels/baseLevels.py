"""
A File to hold all of our Filters
"""

import re
import html

import flask
import markdown

#import xss_trainer.app as app

import xss_trainer.levels.meta as meta


class Training(meta.BaseLevel):
    """
    Our initial Training Level
    """
    levelname = "Tutorial"
    template = "intro.html"


class NoFilter(meta.BaseLevel):
    """
    Apply no filter to the input
    """
    levelname = "No Filter"
    template = "noFilter.html"
    flag = "CUEH{Made_It_Past_Level_1}"
    author = "Dang42"


class ClientFilter(meta.BaseLevel):
    """
    In this level we protect by making sure the user submits an email
    """
    levelname = "Client Side Filter"
    template = "ClientSide.html"
    author = "Dang42"


class SimpleReplace(meta.BaseLevel):
    """
    Replace just <script>
    """
    levelname = "Simple Replace"
    template = "SimpleReplace.html"
    author = "Dang42"

    def sanitise(self, data):
        payload = data.replace("<script>", "")
        payload = payload.replace("</script>", "")
        return payload


class BasicRegexp(meta.BaseLevel):
    """
    Classic regexp replace python version
    """
    levelname = "Basic Regexp"
    template = "BasicRegexp.html"
    author = "Dang42"

    def sanitise(self, data):
        regexp = re.compile("<\/?script>", re.IGNORECASE)
        payload = regexp.sub("", data)
        return payload


class BasicPHPRegexp(meta.BaseLevel):
    """
    Clasic PHP based simple preg_replace
    """

    levelname = "Basic preg_replace"
    template = "BasicPreg.html"
    author = "Dang42"

    def sanitise(self, data):

        theStr = ['$input = "{0}"'.format(data),
                  '$output = preg_replace("/<script>/i","", $input)',
                  '$output = preg_replace("/<\/script>/i","", $output)',
                  'echo $output']
        payload = meta.evalPhp(theStr)
        return payload


class ScriptTagFilter(meta.BaseLevel):
    """
    Remove just the script tags.  One of my favourites
    """

    levelname = "Script tag Filter"
    template = "ScriptTagFilter.html"
    author = "Dang42"

    def sanitise(self, data):
        regexp = re.compile("script", re.IGNORECASE)
        if regexp.search(data):
            return "<div class='alert alert-critical'>XSS Detected!</div>"
        return data


class MarkdownOutput(meta.BaseLevel):
    """
    XSS through markdown
    Turns out new markdown has broken the way I used to do this so we need
    the old legacy_attrs until I work it back out
    """

    levelname = "Output Formats"
    template = "MarkdownOutput.html"
    author = "Dang42"

    def sanitise(self, data):
        clean = html.escape(data)
        payload = markdown.markdown(clean, extensions=['legacy_attrs'])

        return payload


class TagAttributes(meta.BaseLevel):
    """
    XSS Through manipulating tags
    """
    levelname = "Tag Attributes"
    template = "TagAttributes.html"
    author = "Dang42"

    def sanitise(self, data):
        attributes = flask.request.form.get("attributes", "")
        clean = html.escape(data, quote=True)
        payload = f"<details {attributes}>{clean}</details>"
        return payload


class BootstrapTags(meta.BaseLevel):
    """
    XSS through bootstrap CSS animations
    """

    levelname = "More Tag Attributes"
    template = "BootstrapTags.html"
    author = "Dang42"

    def sanitise(self, data):
        alertLevel = flask.request.args.get("style", "primary")
        clean = html.escape(data)
        level = alertLevel
        payload = "<div class='spinner-border text-{1}' role='status'></div>{0}".format(
            clean, level)
        return payload

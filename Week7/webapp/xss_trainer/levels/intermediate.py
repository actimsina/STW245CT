"""
Levels that deal with Sessions and other fun things
"""


import xss_trainer.levels.meta as meta


class SessionTest(meta.BaseLevel):
    """
    A testing level for Sessions
    """
    levelname = "Session Tokens"
    template = "sessionTest.html"
    author = "Dang42"
    #Need to be key value
    cookie = ["xss_session", "FakeSessionCookie"]
    flag = "CUEH{CookieSubmit}"
#    renderer = "customRender.html"

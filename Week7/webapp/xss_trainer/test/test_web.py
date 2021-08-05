"""
Integration testing for the web app

TODO:  Test for Session Jacking
TODO:  Test for Render Function

"""

import unittest
import requests

import xss_trainer.views as views


BASEURL = "http://127.0.0.1:5000"
LEVEL_URL = "http://127.0.0.1:5000/level/"
        

class IntergrationTests(unittest.TestCase):

    def setUp(self):
        """
        Setup,  Do the initial request and get the Session
        """

        self.session = requests.session()
        r = self.session.get(BASEURL)
        self.assertEqual(r.status_code, 200)

    def test_home(self):
        """
        Can we get the homepage
        """

        r = self.session.get(BASEURL)
        self.assertEqual(r.status_code, 200)
        self.assertIn("Learn About XSS.   Break some filters", r.text)
        

    def test_level_zero_get(self):
        """
        Get the first level
        """
        levelURL = "{0}{1}".format(LEVEL_URL, 0)
        
        r = self.session.get(levelURL)
        self.assertIn("Tutorial", r.text)
        self.assertIn("This tutorial will run you through the concepts", r.text)
        self.assertIn("Your Current Max Level is 0", r.text)
        
    def test_level_zero_submit(self):
        """
        submit the first level
        """
        
        levelURL = "{0}{1}".format(LEVEL_URL, 0)
        
        r = self.session.get(levelURL)
        self.assertIn("Tutorial", r.text)
        self.assertIn("This tutorial will run you through the concepts", r.text)

        payload = "<script>alert(1)</script>"
        r = self.session.post(levelURL, data={"payload":payload})
        self.assertEqual(200, r.status_code)

        self.assertIn("Success! You triggered an alert", r.text)
        self.assertIn("Your Current Max Level is 1", r.text)

    def test_access_fails(self):
        """
        Do we get a 403 if we cant access the level
        """
        
        levelURL = "{0}{1}".format(LEVEL_URL, 2)

        r = self.session.get(levelURL)
        self.assertEqual(r.status_code, 403)


    def test_getFlag(self):
        """
        Does completing a level give us a flag
        """

        #First we need to bump up a level
        r = self.session.get("{0}/konami".format(BASEURL))
        
        levelURL = "{0}{1}".format(LEVEL_URL, 1)
        payload = "<script>alert(1)</script>"
        r = self.session.post(levelURL, data={"payload":payload})
        self.assertEqual(200, r.status_code)

        self.assertIn("Have a flag: CUEH{Made_It_Past_Level_1}", r.text)
        

    def test_cookieSubmit(self):
        """
        Can we test if a cookie submission works.

        This test case checks if a cookie submission will show the flag 
        associated with the level.
        """
        
        #Idea with cookie levels is the page checks the cookie value
        #Therefore we can have a check on the page for this, to show a flag

        for idx, item in enumerate(views.LEVELS):
            if item.levelname == "Session Tokens":
                print ("Item found at index {0}".format(idx))
                break


        self.assertEqual(item.template, "sessionTest.html")
        self.assertEqual(item.cookie, ["xss_session", "FakeSessionCookie"])
        
        #So now we can test the submission of the cookie code
        
        #We need a fresh session here, as we are going to want to remove cookies later
        session = requests.session()
        #Find the correct level
        r = session.get("{0}/konami".format(BASEURL))

        levelURL = "{0}{1}".format(LEVEL_URL, idx)
        r = session.get(levelURL)
        self.assertIn("Session Jacking", r.text)
        self.assertNotIn("Flag: CUEH", r.text)
        #Now we set the cookie
        session.cookies.set(item.cookie[0],item.cookie[1])
        r = session.get(levelURL)
        self.assertIn("Flag: CUEH{CookieSubmit}", r.text)
        

    def testGrabCookie(self):
        """
        TODO:  Work out how the heck can i test this
        """

        
        for idx, item in enumerate(views.LEVELS):
            if item.levelname == "Session Tokens":
                print ("Item found at index {0}".format(idx))
                break


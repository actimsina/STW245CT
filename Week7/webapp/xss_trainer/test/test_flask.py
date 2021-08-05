"""
Can we test Flask
"""

import unittest

import flask

from xss_trainer.meta import app
import xss_trainer.views


class PageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config['SERVER_NAME'] = 'localhost:5000'
        app.config["TESTING"] = True
        cls.client = app.test_client()

    def setUp(self):
        """
        Create a flask Application before each run
        """
        #And a Context which is needed for the Sessions etc
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        """
        REmove the context
        """
        self.app_context.pop()
        
    def test_index(self):
        """
        Can we get the index page
        """
        thePage = self.client.get("/")
        self.assertEqual(thePage.status_code, 200)
        
        #Does the Page contain the correct heading
        self.assertIn(b"XSS Trainer", thePage.data)

        #And the text above the level list
        self.assertIn(b"A set of challenge style levels", thePage.data)

    def test_author(self):
        """
        Does adding an Author make a difference
        """
        with self.client.session_transaction() as sess:
            sess["level"] = 2
        thePage = self.client.get(flask.url_for("levels", levelId=1))
        self.assertIn(b"Dang42", thePage.data)

    def test_urlfor(self):
        
        thePage = self.client.get(flask.url_for("main"))
        self.assertEqual(thePage.status_code, 200)
        #And test the session

        
        #self.assertEqual(flask.session["level"] , 0)
        self.assertIn(b"XSS Trainer", thePage.data)

        #And the text above the level list
        self.assertIn(b"A set of challenge style levels", thePage.data)

    def test_initSession(self):
        """
        When it comes to testing sessions we need to so something a bit more funky
        and to keep the testing context around
        """        
        with app.test_client() as client:
            thePage = client.get("/")
            self.assertEqual(flask.session["level"] , 0)

    def test_level(self):
        """
        Can we get a single level
        We will grab the first one (0) as the session wont let others
        """
        
        thePage = self.client.get(flask.url_for("levels"))
        self.assertEqual(thePage.status_code, 200)
        
        self.assertIn(b"Tutorial", thePage.data)

    def test_level_denied(self):
        """
        Do we get level Denied if we ask for something above our 
        current level
        """
        thePage = self.client.get(flask.url_for("levels", levelId=5))
        self.assertEqual(thePage.status_code, 403)

    def test_level_nonexist(self):
        """
        Do we get 404 if the level doesn't exist
        """
        thePage = self.client.get(flask.url_for("levels", levelId=500))
        self.assertEqual(thePage.status_code, 404)

        
    def test_levelNumber(self):
        """
        Can we grab level 3

        This is the Client Side test so it should stick out
        """

        #Manually set the level cookie
        with self.client.session_transaction() as sess:
            sess["level"] = 2
        thePage = self.client.get(flask.url_for("levels", levelId=2))
        self.assertEqual(thePage.status_code, 200)
            
        self.assertIn(b"client side filtering", thePage.data)

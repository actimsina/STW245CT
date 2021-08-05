"""
Unit Tests for the Driver

NOTE:  This will need a selenium instance to connect to
"""

import unittest

import xss_trainer


class DriverTest(unittest.TestCase):

    def testText(self):
        """
        Can we get the Text from a page
        """
        
        driver = xss_trainer.webdriver.SelenoidDriver("http://127.0.0.1:4444/wd/hub")
        self.assertTrue(driver)

        #Fetch a page
        result = driver.getPage("https://httpbin.org/get")
        print (result)
        self.assertTrue(result)


        

"""
Class to check for XSS using Selenium

https://stackoverflow.com/questions/42950789/selenium-open-local-files
"""

import logging

from flask.logging import default_handler

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import selenium

#Create the options we will pass to the driver
opt = webdriver.ChromeOptions()
opt.headless = True

class SelenoidDriver(object):
    """Driver object for Selenoid

    This class deals with talking to the selenoid browser automation
    system It allows us to connect to a service through chrome and
    check for alerts (or other things) on the page.
    """

    def __init__(self, selenoidURL='http://selenoid:4444/wd/hub'):
        """Create the Driver

        @param selenoidURL: Address of remote selenoid server
        """
        self.selenoidURL = selenoidURL

        self.log = logging.getLogger("DRIVER")
        self.log.addHandler(default_handler)
        self.log.setLevel(logging.DEBUG)
        self.log.info("Selenoid Driver Initialised for %s", self.selenoidURL)

    def _fetchPage(self, thePage):
        """

        Lets stick this in one method
        As I am reusing it for the getPage and checkPage

        @param thePage:  URL to test
        @return: Tuple of
            - The Page Text
            - If the page has an alert on it
        """
        self.log.debug("Creating Driver")
        driver = webdriver.Remote(command_executor=self.selenoidURL,
                                  desired_capabilities=DesiredCapabilities.CHROME,
                                  options = opt)

        self.log.debug("Fetch Page")
        driver.get(thePage)
        #Check for XSS
        hasAlert = False
        self.log.debug("Looking for Alert")
        try:
            alert = driver.switch_to.alert
            alert.accept()
            self.log.info("Alert found")
            hasAlert = True
        except selenium.common.exceptions.NoAlertPresentException:
            self.log.info("No Alert")

        #This needs to be after we have handled any alerts
        pageText = driver.page_source

        #Important otherwise we end up with 10^N Chromes
        driver.close()
        driver.quit()

        return pageText, hasAlert

    def getPage(self, thePage):
        """
        Get a page and return its source

        @param thePage: URL to check
        @return: The page source
        """
        pageText, hasAlert = self._fetchPage(thePage)

        return pageText


    def checkPage(self, thePage):
        """
        Get a page and check for XSS

        @param thePage: URL to Check
        @return: If an alert was triggered
        """

        pageText, hasAlert = self._fetchPage(thePage)
        return hasAlert

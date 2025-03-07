#Press the green button in the gutter to run the script.
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from Dropdown import Dropdown
from Homepage import Homepage
from Inputs import Inputs

class SunblazeSelenium(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.driver = webdriver.Chrome(service=Service("./resources/chromedriver/chromedriver.exe"))

    def tearDown(self):
        """Call after every test case."""
        time.sleep(2)
        self.driver.quit()

    def testOpenHomepage(self):
        """Integer Operations
        Note that all test method names must begin with 'test.'"""
        #self.driver.get('https://the-internet.herokuapp.com/')
        homePage = Homepage(self.driver)
        verifyHomePage = homePage.GetText(homePage._txtHomePagetitle)
        assert(verifyHomePage == "Welcome to the-internet")

    def testInputNumbers(self):
        """test case B"""
        inputs = Inputs(self.driver)
        inputs.FieldSendKeys(inputs.inputNumber, "23")

    def testSelectFromDropdown(self):
        """String OperationsB"""
        dropdown = Dropdown(self.driver)
        dropdown.SelectByTextDropdown(dropdown.dropdownField, "Option 2")
        # So we can observe it actually changed
        time.sleep(1)
        dropdown.SelectByTextDropdown(dropdown.dropdownField, "Option 1")


if __name__ == '__main__':
    unittest.main()

#Press the green button in the gutter to run the script.
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

from AddRemove import AddRemove
from Dropdown import Dropdown
from Homepage import Homepage
from Inputs import Inputs
from SortableDataTables import SortableDataTables


class SunblazeSelenium(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

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
        assert verifyHomePage == "Welcome to the-internet"

    def testAddRemove(self):
        """test case B"""
        addRemove = AddRemove(self.driver)
        timesClick = 3
        addRemove.ClickMultiple(addRemove._btnAddElement, timesClick)
        time.sleep(1)
        numDeleteButtons = len(addRemove.GetElements(addRemove._btnDeleteElement))
        assert numDeleteButtons == timesClick
        addRemove.ClickMultiple(addRemove._btnDeleteElement, timesClick - 1)
        remainingDeleteButtons = len(addRemove.GetElements(addRemove._btnDeleteElement))
        assert remainingDeleteButtons == 1
        time.sleep(1)

    def testSelectFromDropdown(self):
        """String OperationsB"""
        dropdown = Dropdown(self.driver)
        dropdown.SelectByTextDropdown(dropdown.dropdownField, "Option 2")
        # So we can observe it actually changed
        time.sleep(1)
        dropdown.SelectByTextDropdown(dropdown.dropdownField, "Option 1")

    def testInputNumbers(self):
        """test case B"""
        inputs = Inputs(self.driver)
        inputs.FieldSendKeys(inputs.inputNumber, "23")

    def testSortableDataTables(self):
        """test case B"""
        sortableDataTables = SortableDataTables(self.driver)
        initialTable = sortableDataTables.GetTable(sortableDataTables._tblTable1)
        # Sort by Last Name Ascending and check if data matches
        sortByValue = "Last Name"
        tableDataSortedAsc = sortableDataTables.TableDataSortedBy(initialTable, sortByValue, True)
        sortableDataTables.SortTableBy(sortByValue)
        sortedTableAsc = sortableDataTables.GetTable(sortableDataTables._tblTable1)
        assert tableDataSortedAsc == sortedTableAsc
        # Sort by Last Name Descending and check if data matches
        tableDataSortedDesc = sortableDataTables.TableDataSortedBy(initialTable, sortByValue, False)
        sortableDataTables.SortTableBy(sortByValue)
        sortedTableDesc = sortableDataTables.GetTable(sortableDataTables._tblTable1)
        assert tableDataSortedDesc == sortedTableDesc
        print(f"{sortedTableAsc}")


if __name__ == '__main__':
    unittest.main()

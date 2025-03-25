from selenium.webdriver.common.by import By
from Homepage import Homepage

class SortableDataTables(Homepage):
    _tblTable1 = (By.XPATH, "//table[@id='table1']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        super().ClickOn(super()._lnkSortableDataTables)

    def GetTable(self, by):
        allTableData = []
        # Get Headers which will make sorting easier
        # Dynamic XPath expression using base table XPath + path to headers
        tableHeadersLoc = (By.XPATH, f"{self._tblTable1[1]}/thead/tr/th")
        allHeaderElements = super().GetElements(tableHeadersLoc)
        allHeaderNames = []
        for header in allHeaderElements:
            headerName = header.text
            allHeaderNames.append(headerName)
        # Get List of all rows
        rowLoc = (By.XPATH, f"{self._tblTable1[1]}/tbody/tr")
        allRowsElements = super().GetElements(rowLoc)
        # Starting from 1 as XPath index starts from 1, also for Python add 1 to elements length
        for i in range(1, len(allRowsElements) + 1):
            # Iterating over each row in table
            specificRowLoc = f"{self._tblTable1[1]}/tbody/tr[{i}]"
            # Locating only cells of specific row.
            allColumnsElements = self.driver.find_element(By.XPATH, specificRowLoc).find_elements(By.TAG_NAME, "td")
            # Creating a Dictionary to store key-value pair data
            eachRowData = {}
            # Iterating over each cell in row
            for j in range(len(allColumnsElements)):
                # Get cell value and create new Dictionary entry of pair {header name : cell value}
                cellValue = allColumnsElements[j].text
                eachRowData.update({allHeaderNames[j]: cellValue})
            # Add Dictionary of row to list
            allTableData.append(eachRowData)
        return allTableData

    def TableDataSortedBy(self, tableData, sortByValue, orderAsc):
        sortedTable = []
        # Create a Dictionary of original index order and corresponding Column value, => {0, "Smith"}{1, "Bach"}{2, "Doe"}{3, "Conway"}
        unsortedValues = {}
        iterator = 0
        for item in tableData:
            unsortedValues.update({iterator: item.get(sortByValue)})
            iterator += 1
        #Sort the map by its values => {1, "Bach"}{3, "Conway"}{2, "Doe"}{0, "Smith"}
        #Order by Ascending or Descending, depending on value of orderAsc boolean
        sortedByValueMap = sorted(unsortedValues, key=unsortedValues.get) if orderAsc else sorted(unsortedValues, key=unsortedValues.get, reverse=True)
        #Add values to sortedTable using order and keys from sortedByValueMap
        for entry in sortedByValueMap:
            sortedTable.append(tableData[entry])
        return sortedTable

    def SortTableBy(self, sortByValue):
        sortLoc = (By.XPATH, f"{self._tblTable1[1]}/thead/tr/th/span[text()='{sortByValue}']")
        super().ClickOn(sortLoc)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Homepage(object):
    # Locators are stored in tuple for Python since By type is not a string
    _txtHomePagetitle = (By.XPATH, "//h1[text()='Welcome to the-internet']")
    _lnkAddRemove = (By.XPATH, "//a[text()='Add/Remove Elements']")
    _lnkDropdown = (By.XPATH, "//a[text()='Dropdown']")
    _lnkInputs = (By.XPATH, "//a[text()='Inputs']")
    _lnkSortableDataTables = (By.XPATH, "//a[text()='Sortable Data Tables']")

    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://the-internet.herokuapp.com/')

    def ClickOn(self, by):
        # Find element takes By type as first argument and value as second
        self.driver.find_element(by[0], by[1]).click()

    def ClickMultiple(self, by, num):
        while num > 0:
            self.driver.find_element(by[0], by[1]).click()
            num -= 1

    def FieldSendKeys(self, by, inputValue):
        self.driver.find_element(by[0], by[1]).send_keys(inputValue)

    def GetText(self, by):
        return self.driver.find_element(by[0], by[1]).text

    def GetElements(self, by):
        return self.driver.find_elements(by[0], by[1])

    def SelectByTextDropdown(self, by, text):
        selectElement = Select(self.driver.find_element(by[0], by[1]))
        selectElement.select_by_visible_text(text)

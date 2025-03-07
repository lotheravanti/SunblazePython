from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Homepage(object):
    _txtHomePagetitle = (By.XPATH, "//h1[text()='Welcome to the-internet']")
    _lnkInputs = (By.XPATH, "//a[text()='Inputs']")
    _lnkDropdown = (By.XPATH, "//a[text()='Dropdown']")

    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://the-internet.herokuapp.com/')

    def ClickOn(self, by):
        self.driver.find_element(by[0], by[1]).click()

    def FieldSendKeys(self, by, inputValue):
        self.driver.find_element(by[0], by[1]).send_keys(inputValue)

    def GetText(self, by):
        return self.driver.find_element(by[0], by[1]).text

    def SelectByTextDropdown(self, by, text):
        selectElement = Select(self.driver.find_element(by[0], by[1]))
        selectElement.select_by_visible_text(text)

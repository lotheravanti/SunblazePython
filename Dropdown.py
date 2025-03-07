from selenium.webdriver.common.by import By
from Homepage import Homepage

class Dropdown(Homepage):
    dropdownField = (By.ID, "dropdown")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        super().ClickOn(super()._lnkDropdown)

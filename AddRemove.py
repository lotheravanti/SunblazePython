from selenium.webdriver.common.by import By
from Homepage import Homepage

class AddRemove(Homepage):
    _btnAddElement = (By.XPATH, "//button[text()='Add Element']")
    _btnDeleteElement = (By.XPATH, "//button[text()='Delete']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        super().ClickOn(super()._lnkAddRemove)

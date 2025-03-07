from selenium.webdriver.common.by import By
from Homepage import Homepage

class Inputs(Homepage):
    inputNumber = (By.XPATH, "//div/p[text()='Number']/following-sibling::input[1]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        super().ClickOn(super()._lnkInputs)

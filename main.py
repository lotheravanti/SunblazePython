from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


def test_url():
    driver = webdriver.Chrome(service=Service("./resources/chromedriver/chromedriver.exe"))
    driver.get('https://the-internet.herokuapp.com/')
    time.sleep(5)
    driver.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_url()



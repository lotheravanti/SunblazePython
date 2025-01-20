# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def test_url():
    driver = webdriver.Chrome(service=Service("./resources/chromedriver/chromedriver.exe"))
    driver.get('https://the-internet.herokuapp.com/')
    time.sleep(5)
    driver.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Sunblaze Tester')
    test_url()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

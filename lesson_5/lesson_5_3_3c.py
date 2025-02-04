from selenium import webdriver
from time import sleep 

chrome = webdriver.Chrome()

try:
    chrome.get("http://uitestingplayground.com/classattr")
    for _ in range(3):
        blue_button = chrome.find_element(
            "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
        blue_button.click()
        sleep(1)
        chrome.switch_to.alert.accept()
except Exception as ex:
    print(ex)
finally:
    chrome.quit()
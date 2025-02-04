from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep 

chrome = webdriver.Chrome()

try:
    chrome.get("http://the-internet.herokuapp.com/add_remove_elements/")
    for _ in range(5):
        add_button = chrome.find_element(
            By.XPATH, '//button [text()="Add Element"]').click()
        sleep(1)
        chrome_delete_buttons = chrome.find_elements(
            "xpath", '//button [text()="Delete"]')   
    print(
        f"Chrome: {len(chrome_delete_buttons)}")
except Exception as ex:
    print(ex)
finally:
    chrome.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep 

chrome = webdriver.Chrome()

try:
    chrome.get("http://the-internet.herokuapp.com/login")
    input_name = chrome.find_element(
        By.ID, "username").send_keys("olegt")
    sleep(2)
    input_pass = chrome.find_element(
        By.ID, "password").send_keys("secret")
    sleep(1)
    button = chrome.find_element(
        By. TAG_NAME, "button").click()
    sleep(2)

except Exception as ex:
    print(ex)
finally:
    chrome.quit()
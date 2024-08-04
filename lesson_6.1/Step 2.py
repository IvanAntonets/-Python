from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

chrome = webdriver.Chrome()

try:
    chrome.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    delay_input = chrome.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys(45)

    for _ in range(1):
        button = chrome.find_element(
            By.XPATH, '//span[text() = "7"]').click()
        button = chrome.find_element(
            By.XPATH, '//span[text() = "+"]').click()
        button = chrome.find_element(
            By.XPATH, '//span[text() = "8"]').click()
        button = chrome.find_element(
            By.XPATH, '//span[text() = "="]').click() 
        
    WebDriverWait(chrome,46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
    result_text = chrome.find_element(By.CLASS_NAME, "screen").text
    sleep(3)
    print(result_text)
except Exception as ex:
    print(ex)
finally:
    chrome.quit()
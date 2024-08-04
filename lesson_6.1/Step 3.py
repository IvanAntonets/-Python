from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

chrome = webdriver.Chrome()

try: 
    chrome.get("https://www.saucedemo.com/")
    chrome.find_element(By.ID, "user-name").send_keys("standart_user")
    chrome.find_element(By.ID, "password").send_keys("secret_sauce")
    chrome.find_element(By.ID, "login_button").click()
    chrome.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    chrome.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    chrome.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    chrome.find_element(By.ID, "shopping_cart_container").click()
    chrome.find_element(By.ID, "checkout").click()
    chrome.find_element(By.ID, "first-name").send_keys("Igor")
    chrome.find_element(By.ID, "last-name").send_keys("Petrosyan")
    chrome.find_element(By.ID, "postal-code").send_keys("897526")
    chrome.find_element(By.ID, "continue").click()
    total_price = chrome.find_element(By.CLASS_NAME, 'summary_total_label')
    total = total_price.text.strip().replace("Total: $", "")

    excepted_total = "58.29"
    assert total == excepted_total
    print("ИТОГОВАЯ СУММА РАВНА $58.29")
    sleep(3)

except Exception as ex:
    print(ex)
finally:
    chrome.quit()
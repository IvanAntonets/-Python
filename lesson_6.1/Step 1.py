from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from configuration import *
from time import sleep

chrome = webdriver.Chrome()

def test_data_types_form(chrome):
    chrome.get(URL_1)
    chrome.find_element(By.NAME, "first-name").send_keys(first_name)
    chrome.find_element(By.NAME, "last-name").send_keys(last_name)
    chrome.find_element(By.NAME, "address").send_keys(address)
    chrome.find_element(By.NAME, "e-mail").send_keys(email)
    chrome.find_element(By.NAME, "phone").send_keys(phone)
    chrome.find_element(By.NAME, "zip-code").send_keys(zip_code)
    chrome.find_element(By.NAME, "city").send_keys(city)
    chrome.find_element(By.NAME, "country").send_keys(country)
    chrome.find_element(By.NAME, "job-position").send_keys(job_position)
    chrome.find_element(By.NAME, "company").send_keys(company)
WebDriverWait(chrome, 40, 0.1).until(EC.element_to_be_clickable((By.TAG_NAME, "button")))
sleep(3)
assert "danger" in chrome.find_element(By.ID, "zip-code").get_atribute("class")
assert "success" in chrome.find_element(By.ID, "first-name").get_atribute("class")
assert "success" in chrome.find_element(By.ID, "last-name").get_atribute("class")
assert "success" in chrome.find_element(By.ID, "address").get_atribute("class")
assert "success" in chrome.find_element(By.ID, "e-mail").get_atribute("class")
assert "success" in chrome.find_element(By.ID, "phone").get_atribute("class")
assert "success" in chrome.find_element(By.ID, "city").get_atribute("class")
assert "success" in chrome.find_element(By.ID, "country").get_atribute("class")
assert "success" in chrome.find_element(By.ID, "job-position").get_atribute("class")
assert "success" in chrome.find_element(By.ID, "company").get_atribute("class")

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

firefox = webdriver.Chrome()

try:
    firefox.get("http://the-internet.herokuapp.com/entry_ad")
    wait = WebDriverWait(firefox, 10)
    modal_window = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal")))
    close_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-footer")))
    time.sleep(1)
   
except Exception as ex:
    print(ex)
finally:
    firefox.quit()
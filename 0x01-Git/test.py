import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.google.com/")
time.sleep(5)

google_search_box = driver.find_element(By.ID, "APjFqb")
google_search_box.send_keys("Selenium")

time.sleep(3)

google_search_btn = driver.find_element(By.NAME, "btnK")
google_search_btn.click()
time.sleep(5)

driver.close()
driver.quit()

print("Testing done")
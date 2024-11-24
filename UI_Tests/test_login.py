from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://github.com/login")

driver.find_element(By.ID, "login_field").send_keys("your_email")
driver.find_element(By.ID, "password").send_keys("your_password")
driver.find_element(By.NAME, "commit").click()

driver.quit()

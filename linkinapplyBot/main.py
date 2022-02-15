from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

ACCOUNT_EMAIL = os.environ.get("L_NAME")
ACCOUNT_PASSWORD = os.environ.get("L_PASS")

print(ACCOUNT_EMAIL)
print(ACCOUNT_PASSWORD)
chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=2918703334&geoId=102095887&keywords=python%20developer&location=California%2C%20United%20States")

sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()


time.sleep(5)
input_email = driver.find_element_by_id("username")
input_email.send_keys(ACCOUNT_EMAIL)
input_password = driver.find_element_by_id("password")
input_password.send_keys(ACCOUNT_PASSWORD)
input_password.send_keys(Keys.ENTER)

time.sleep(5)
Easy_apply_button = driver.find_element_by_xpath(
    "/html/body/div[6]/div[3]/div[3]/section/div/div/div/ul/li[8]/div/button")
Easy_apply_button.click()

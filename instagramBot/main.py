
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
USER_NAME = os.environ.get('INSTAGRAM_NAME')
USER_PASS = os.environ.get('INSTAGRAM_PASS')
CHROME_DRIVER_PATH = os.environ.get('CHROME_DRIVER_PATH')
class InstaFollower:
    def __init__(self,path) -> None:
        self.driver = webdriver.Chrome(executable_path=path)
        
    
    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(2)
        input_username = self.driver.find_element_by_css_selector("[aria-label='Phone number, username, or email']")
        input_username.send_keys(USER_NAME)
        input_password = self.driver.find_element_by_css_selector("[aria-label='Password']")
        input_password.send_keys(USER_PASS)
        input_password.send_keys(Keys.ENTER)
        time.sleep(2)
        click_next = self.driver.find_element_by_css_selector(
            "#react-root > section > main > div > div > div > div > button")
        click_next.click()
        time.sleep(2)
        click_next = self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.bIiDR")
        click_next.click()
        
    def find_follower(self):
        time.sleep(2)
        self.driver.get('https://www.instagram.com/interiordesignmag/')
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div').click()
        time.sleep(2)
        bar_scoll = self.driver.find_element_by_xpath(
            "/html/body/div[6]/div/div/div/div[2]")
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", bar_scoll)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector(
            "li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath(
                    "/html/body/div[7]/div/div/div/div[3]/button[2]")
                cancel_button.click()
                time.sleep(2)
        print ("Followed all") 
        exit_button = self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[1]/div/div[2]/button")
        exit_button.click()
        


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_follower()
bot.follow()

from selenium import webdriver
import os 
import time
PROMISE_DOWN= "940"
PROMISE_UP = "880"
chrome_driver_path = "C:\Development\chromedriver.exe"
from selenium.webdriver.common.keys import Keys
TWITTER_NAME = os.environ.get('TWITTER_NAME')
TWITTER_PASS = os.environ.get('TEST_PASSWORD_TWITTER')


class InternetSpeedTwitterBot:
    def __init__(self,driver_path):
        self.driver= webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0        
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        go_button = self.driver.find_element_by_css_selector(".start-button a")
        go_button.click()
        time.sleep(60)
        self.down = self.driver.find_element_by_xpath(
            "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text
        self.up = self.driver.find_element_by_xpath(
            "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span"
        ).text
        close_ad = self.driver.find_element_by_xpath(
            "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a"
        )
        if close_ad:
            close_ad.click()
            
    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
       
        print("starting login")
        time.sleep(5)
        email_auth = self.driver.find_element_by_xpath(
            "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input")
        email_auth.send_keys(TWITTER_NAME)
        time.sleep(2)
        next_button = self.driver.find_element_by_xpath(
            "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div")
        next_button.click()
        time.sleep(2)
        print("entering password")
        password_auth = self.driver.find_element_by_xpath(
            "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input")
        password_auth.send_keys(TWITTER_PASS)
        time.sleep(2)
        password_auth.send_keys(Keys.ENTER)
        time.sleep(2)
        print("attempting to tweet")
        button_add_tweet = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a")
        time.sleep(2)
        button_add_tweet.click()
        time.sleep(2)
        input_message = self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div")
        message_will_send = f"Internet speed is {self.down} down and {self.up} up and My ATT internet provider promises for 1000 fiber is {PROMISE_DOWN} down and {PROMISE_UP} up"
        input_message.send_keys(message_will_send)
        time.sleep(3)
        tweet_button = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div")
        tweet_button.click()
        time.sleep(2)
        print("succeeded")
        self.driver.quit()
        
bot = InternetSpeedTwitterBot(chrome_driver_path)
bot.get_internet_speed()
bot.tweet_at_provider()

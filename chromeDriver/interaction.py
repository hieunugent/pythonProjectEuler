from selenium import webdriver
chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
from selenium.webdriver.common.keys import Keys

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element_by_css_selector("#articlecount a")

# article_count.click()


all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()


search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# driver.close()
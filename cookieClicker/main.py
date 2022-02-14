import time
from selenium import webdriver
chrome_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")


cookie_pie = driver.find_element_by_id("cookie")
shop_list = ["Cursor", "Grandma", "Factory", "Mine",
             "Shipment", "Alchemy lab", "Portal", "Time machine"]
def refresh():
    global shop, shop_amount 
    shop = [driver.find_element_by_id(f"buy{name}") for name in shop_list]
    shop_amount = [
        int(driver.find_element_by_xpath(f'//*[@id="buy{name}"]/b').text.split()[-1].replace(',','')) for name in shop_list]
    print(shop_amount)
   
refresh()
items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5

five_min = time.time() +60*5

while True:
    cookie_pie.click()
    if time.time() > timeout:
        all_prices = driver.find_elements_by_css_selector("#store b")
        item_prices=[]
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = element_text.split("-")[1].strip().replace(",","")
                item_prices.append(int(cost))
        cookie_upgrades={}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]
        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",","")
        cookie_count = int(money_element)
        
        
        affordable_upgrades ={}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id 
                
                
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
        
        driver.find_element_by_id(to_purchase_id).click()
        timeout = time.time()+5
    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break

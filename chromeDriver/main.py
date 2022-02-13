chrome_driver_path = "C:\Development\chromedriver.exe"
from selenium import webdriver
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ/?_encoding=UTF8&pd_rd_w=C9joB&pf_rd_p=9da53265-487a-4d6a-98d4-d119016236b9&pf_rd_r=D5DSGYXGADMZEXJMEW51&pd_rd_r=7653d4d5-2f08-45ab-b8b7-c18d2383550c&pd_rd_wg=hoMHu&ref_=pd_gw_ci_mcx_mr_hp_atf_m&th=1")

price = driver.find_element_by_id("corePrice_desktop").text

price_only = price.split(" ")[0].split(":")[1]
print(price_only)





driver.quit()

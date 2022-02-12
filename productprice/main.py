from unittest import result
from urllib import response
import requests
import lxml 
from bs4 import BeautifulSoup
import os

item_url = "https://www.amazon.com/Instant-Pot-Plus-Programmable-Sterilizer/dp/B075CWJ3T8/ref = dp_fod_3?pd_rd_i = B075CWJ3T8 & psc = 1"

headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"
}

response = requests.get(item_url, headers=headers)


soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())
price = soup.find(id ="corePrice_desktop").get_text()
price_without_currency = price.split("$")[1]

price_as_float = float(price_without_currency)
print(price_as_float)

import smtplib

title = soup.find(id ="productTitle").get_text().strip()
BUY_PRICE = 200
if price_as_float < BUY_PRICE:
    print("System will send Buy Notification to the User!")
    # send an email
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        result = connection.login(os.environ.get('MY_EMAIL_TEST'),os.environ.get('MY_TEST_EMAIL_PASS'))
        connection.sendmail(
            from_addr=os.environ.get('MY_EMAIL_TEST'),
            to_addrs="example@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{title} \n is now available for{price_as_float}\! Buy it now! \n{item_url}"
        )


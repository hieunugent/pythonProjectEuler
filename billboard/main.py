from numpy import tile
import requests
from bs4 import BeautifulSoup
# date= input("Enter the date in the format YYYY-MM-DD: ")
date="2000-08-12"
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")

bb_page = response.text

soup = BeautifulSoup(bb_page, "html.parser")
# print(soup.prettify())
title_ids= soup.select(selector='li h3')
# print(title_ids)

titles = [title_id.get_text().replace("\n", "") for title_id in title_ids][:100]
# print(titles)
# print(len(titles))


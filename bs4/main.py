from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
article_tag = soup.find(name="a", class_="titlelink")
article_text = article_tag.getText()
article_link = article_tag.get('href')
article_upvote = soup.find(name="span", class_="score").getText()

print




























# from bs4 import BeautifulSoup


# with open("bs4/myWeb.html", encoding="utf8") as f :
#     contents = f.read()
    
    
# soup = BeautifulSoup(contents, "html.parser")


# anchor = soup.find_all(name ="a")
# for  tag in anchor:
#     print(tag.get("href"))
    
# heading = soup.find(name = "h1", id="name")
# print(heading)
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))
# name = soup.select_one(selector="#name")
# print(name)
# headings = soup.select(".heading")
# print(headings)

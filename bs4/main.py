from statistics import mode
from urllib import response
from bs4 import BeautifulSoup
import requests

response = requests.get(
    'https://www.imdb.com/list/ls055592025/')
ep_web_page = response.text
soup = BeautifulSoup(ep_web_page, 'html.parser')

list_movies_bucket = soup.find_all(name="h3", class_="lister-item-header")
movie_titles = [(movies.getText().replace("\n", "")) for movies in list_movies_bucket]

with open("bs4/movies.txt", mode="w") as file:
    for movie in movie_titles:
        file.write(movie + "\n")






# from bs4 import BeautifulSoup
# import requests

# response = requests.get("https://news.ycombinator.com/news")
# yc_web_page = response.text

# soup = BeautifulSoup(yc_web_page, 'html.parser')
# articles= soup.find_all(name="a", class_="titlelink")
# article_texts = []
# article_links = []
# for article_tag in articles:
#     text = article_tag.getText()
#     link = article_tag.get('href')
#     article_texts.append(text)
#     article_links.append(link)
# article_upvotes = [
#    int( score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# # print(article_texts)
# # print(article_links)

# largest_number = max(article_upvotes)
# largest_index = article_upvotes.index(largest_number)

# print(article_texts[largest_index])
# print(article_links[largest_index])




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

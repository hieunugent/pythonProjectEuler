
from bs4 import BeautifulSoup


with open("bs4/myWeb.html", encoding="utf8") as f :
    contents = f.read()
    
    
soup = BeautifulSoup(contents, "html.parser")


anchor = soup.find_all(name ="a")
for  tag in anchor:
    print(tag.get("href"))
    
heading = soup.find(name = "h1", id="name")
print(heading)
section_heading = soup.find(name="h3", class_="heading")
print(section_heading.get("class"))
name = soup.select_one(selector="#name")
print(name)
headings = soup.select(".heading")
print(headings)
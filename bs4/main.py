from math import factorial
from bs4 import BeautifulSoup


with open("bs4/myWeb.html") as f :
    contents = f.read()
    
    
# soup = BeautifulSoup(contents, "html.parser")

# print(soup)
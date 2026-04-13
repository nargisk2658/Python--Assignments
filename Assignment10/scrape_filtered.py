import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com/"
res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")

quotes = soup.find_all("div", class_="quote")

for q in quotes:
    author = q.find("small").text
    
    if author == "Albert Einstein":
        print(q.find("span").text)
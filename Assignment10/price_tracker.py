import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

for book in books:
    name = book.find("h3").text
    price = book.find("p", class_="price_color").text

    print(name, "-", price)
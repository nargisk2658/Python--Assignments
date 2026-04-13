import requests
from bs4 import BeautifulSoup
import csv

url = "http://quotes.toscrape.com/"
res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")

quotes = soup.find_all("div", class_="quote")

with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])

    for q in quotes:
        text = q.find("span").text
        author = q.find("small").text
        writer.writerow([text, author])
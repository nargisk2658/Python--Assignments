import requests
from bs4 import BeautifulSoup

url = "https://example.com"

res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

price = "Not Found"

for p in soup.find_all("p"):
    if "₹" in p.text:
        price = p.text

print("Price:", price)
import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")

images = soup.find_all("img")

for i, img in enumerate(images):
    img_url = "http://books.toscrape.com/" + img["src"]
    img_data = requests.get(img_url).content

    with open(f"image_{i}.jpg", "wb") as f:
        f.write(img_data)
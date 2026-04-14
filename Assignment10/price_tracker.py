import requests
from bs4 import BeautifulSoup

# URL of product page
url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

# Headers (important for assignment)
headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    # Step 1: Send request
    response = requests.get(url, headers=headers)

    # Step 2: Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Step 3: Extract price
    price_text = soup.find("p", class_="price_color").text
    print("Extracted price:", price_text)

    # Step 4: Clean price (remove symbols)
    price_clean = price_text.replace("£", "").replace("Â", "").strip()

    # Step 5: Convert to float
    price = float(price_clean)
    print("Clean price:", price)

    # Step 6: Compare with target price
    target_price = 50

    if price < target_price:
        print("Buy now! Price is low 😍")
    else:
        print("Wait... Price is high 😢")

except Exception as e:
    print("Error:", e)
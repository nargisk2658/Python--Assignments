import requests

url = "https://via.placeholder.com/150"

res = requests.get(url)

with open("image.png", "wb") as file:
    file.write(res.content)

print("Image downloaded")
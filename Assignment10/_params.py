import requests

url = "https://httpbin.org/get"

params = {"page": 2, "count": 5}

res = requests.get(url, params=params)

print(res.url)
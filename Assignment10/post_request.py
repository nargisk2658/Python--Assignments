import requests

url = "https://httpbin.org/post"

data = {"username": "test", "password": "123"}

res = requests.post(url, data=data)

print(res.text)
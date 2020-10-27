import requests

res = requests.get('https://ipinfo.io/')
data = res.json()

loc = data['loc']
print(loc)

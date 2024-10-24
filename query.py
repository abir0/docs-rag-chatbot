import requests


url = "http://5.189.136.118:8558/api"
params = {"query": "What are the email ports of the inbox email server?", "k": 3}

response = requests.get(url, params=params)
print(response.json())

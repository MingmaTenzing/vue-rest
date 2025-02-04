import requests
import json
url = "http://127.0.0.1:8000/api/jobs/"

response = requests.get(url)

data = json.load(response)
print(data)
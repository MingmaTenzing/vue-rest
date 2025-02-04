import json 
import requests

with open('jobs.json', 'r', encoding='utf-8') as jobs:
    data = json.load(jobs)

url="http://127.0.0.1:8000/api/jobs/"


for job in data['jobs']: 
    response = requests.post(url, json=job)
    print(response)
    
    
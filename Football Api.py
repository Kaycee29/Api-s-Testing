import requests
import json

url = 'http://api.football-data.org/v4/competitions/'
response = requests.get(url)
response_dict = response.json()
test1 = response_dict['competitions']
Competition_name = []
for test in test1:
    Competition_name.append(test['name'])
print(Competition_name)
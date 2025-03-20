import requests
import json

url = 'https://randomuser.me/api/?results=500'

response = requests.get(url)
response_dict = response.json()


Trial1 =  response_dict['results']

profile_male =  []
profile_female = []
for trial in Trial1:
    if trial['gender'] == 'male':
        profile_male.append(trial)
    elif trial['gender'] == 'female':
        profile_female.append(trial)

male_birth = []
for male in profile_male:
    value = male['dob']
    male_birth.append(value)

male_birth_date = []
for male in male_birth:
    datevalue =  male['date']
    male_birth_date.append(datevalue)

male_full_name = []

for profile in profile_male:
    first_name = profile['name']['first']
    last_name = profile['name']['last']
    full_name = f"{first_name} {last_name}"
    male_full_name.append(full_name)

print(male_full_name)

femalebirth = []
for female in profile_female:
    value = female['dob']
    femalebirth.append(value)
female_birth_date = []
for female in femalebirth:
    datevalue =  female['date']
    female_birth_date.append(datevalue)   

female_full_name = []
for profile in profile_female:
    first_name = profile['name']['first']
    last_name = profile['name']['last']
    full_name = f"{first_name} {last_name}"
    female_full_name.append(full_name)


print('males name:', male_full_name)

print('females name:', female_full_name)

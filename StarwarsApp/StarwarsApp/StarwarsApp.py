import requests
import json

#def full_data():
 #   starwars_data = requests.get('https://swapi.dev/api/')
    # Export the data for use in future steps
  #  return full_data.json()

starwars_data = requests.get('https://swapi.dev/api/')
starwars_people = requests.get('https://swapi.dev/api/people/')

response_people = json.loads(starwars_people.text)
response_data = json.loads(starwars_data.text)

print(response_people)
#print('Hello world')
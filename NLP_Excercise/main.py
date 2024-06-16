import requests
from _datetime import datetime
import os

APP_ID = os.environ["APP_ID"]
APP_KEY = "7215eb448ce325acba56b4ee224fe917"

USERNAME = 'likhitha'
PASSWORD = 'ujhtgrfdsaSDFG6'
TOKEN = 'bGlraGl0aGE6dWpodGdyZmRzYVNERkc2'

headers2 = {
    "Authorization": f"Basic {TOKEN}"
}

GENDER = 'female'
WEIGHT_IN_KG = 53
HEIGHT_IN_CM = 163
AGE = 20

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_json = {
    "query": input("Tell me which exercise you did: "),
    'age': AGE,
    'weight_kg': WEIGHT_IN_KG,
    'height_cm': HEIGHT_IN_CM,
    'gender': GENDER
}

response = requests.post(url=exercise_endpoint, json=exercise_json, headers=headers)
exercise = response.json()['exercises'][0]['name']
calories_burnt = response.json()['exercises'][0]['nf_calories']
duration = response.json()['exercises'][0]['duration_min']

now = datetime.now()
time = now.strftime('%H:%M:%S')
date = now.strftime('%d/%m/%Y')

print(date, time, exercise, duration, calories_burnt)

user_name = '96bbb3630706a0e510b664582697399c'
project_name = 'myExercise'
sheet_name = 'workouts'
# sheety_endpoint = f'https://api.sheety.co/{user_name}/{project_name}/{sheet_name}'
# sheety_response = requests.get(url=sheety_endpoint)
# print(sheety_response.json())
post_endpoint = f'https://api.sheety.co/{user_name}/{project_name}/{sheet_name}'
post_parameters = {
    # singular form of sheet_name
    'workout':
        {
                'date': date,
                'time': time,
                'exercise': exercise.title(),
                'duration': duration,
                'calories': calories_burnt,
                'id': 2
        }
}
# post_response = requests.post(url=post_endpoint, json=post_parameters, auth=(USERNAME, PASSWORD))  -- this also works
post_response = requests.post(url=post_endpoint, json=post_parameters, headers=headers2)
print(post_response.text)


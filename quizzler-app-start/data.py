import requests

response = requests.get(url='https://opentdb.com/api.php?amount=10&type=boolean&category=32')
question_data = response.json()['results']
print(len(question_data))
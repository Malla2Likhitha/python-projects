import requests
from datetime import datetime

x = datetime.now()
# x = datetime(year=2024, month=6, day=2)
date_today = x.strftime("%Y%m%d")

USERNAME = 'likhitha27'
TOKEN = 'zadyesbvnxergdesd'
headers = {
    'X-USER-TOKEN': TOKEN
}
pixela_endpoint = 'https://pixe.la/v1/users'

user_parameters = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
graph_parameters = {
    'id': 'graph1',
    'name': 'My Coding Graph',
    'unit': 'Hours',
    'type': 'float',
    'color': 'ajisai'
}

pixel_endpoint = f"{graph_endpoint}/{graph_parameters['id']}"
pixel_parameters = {
    'date': date_today,
    'quantity': input('How many hours did you read today? ')
}

updated_pixel_endpoint = f'{pixel_endpoint}/{date_today}'
updated_pixel_parameters = {
    'quantity': '8.5'
}

# user_response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(user_response.text)
# graph_response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(graph_response.text)
# pixel_response = requests.post(url=pixel_endpoint, json=pixel_parameters, headers=headers)
# print(pixel_response.text)
updated_pixel_response = requests.put(url=updated_pixel_endpoint, json=updated_pixel_parameters, headers=headers)
print(updated_pixel_response.text)

# user_response = requests.delete(url=graph_endpoint, json=user_parameters, headers=headers)
# print(user_response.text)

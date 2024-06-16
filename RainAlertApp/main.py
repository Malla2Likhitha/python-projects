import requests
from twilio.rest import Client

# account_sid = 'ACfed9e4fee8afc6d035c76461af1c9537'
# auth_token = '333a16efd29725e37dec49a3d4955854'
# MY_TWILIO_PHONE_NO = '+14237197339'
# MY_PHONE_NO = '+918332047072'

api_key = 'e34b1921f2331ce8fd8c7676bbccdd52'
api_endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
parameter = {
    'lat': 13.166000,
    'lon': 75.865601,
    'appid': api_key,
    'cnt': 4
}

response = requests.get(url=api_endpoint, params=parameter)
response.raise_for_status()
# print(response.json()['list'])
weather = response.json()['list']
condition_codes = [i['weather'][0]['id'] for i in weather]
will_rain = False
# print(condition_codes)
for i in condition_codes:
    if i < 700:
        will_rain = True
if will_rain:

    # client = Client(account_sid, auth_token)
    # print("It's gonna rain. Don't forget your ☔🌂.")
    # message = client.messages \
    #     .create(
    #         body="It's gonna rain. Don't forget your ☔🌂.",
    #         from_=MY_TWILIO_PHONE_NO,
    #         to=MY_PHONE_NO
    #     )
    # print(message.status)
    # print(message.body)

    account_sid = 'AC3245e55cd725b448d6a1c19d84d40382'
    auth_token = '719e7381f7c6bc7329682b7864fd5009'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='It\'s gonna rain. Don\'t forget your ☔🌂.',
        to='whatsapp:+918332047072'
    )

    print(message.status)

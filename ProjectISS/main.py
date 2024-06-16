import requests
import datetime as dt
import smtplib
from time import sleep

LATITUDE = 17.385044
LONGITUDE = 78.486671

parameter = {
    # lat, lng are the default parameter names found in api
    'lat': LATITUDE,
    'lng': LONGITUDE,
    'formatted': 0
}

my_email = 'mallalikhitha9@gmail.com'
password = "rkzdqfjnwgvwnflr"

while True:
    sleep(60)
    response1 = requests.get(url='https://api.sunrise-sunset.org/json', params=parameter)
    response1.raise_for_status()
    # +5 for utc to ist.. it's actually 5 hr, 30 min
    sunrise = int(response1.json()['results']['sunrise'].split('T')[1].split(':')[0]) + 5
    sunset = int(response1.json()['results']['sunset'].split('T')[1].split(':')[0]) + 5

    print(sunrise)
    print(sunset)
    now = dt.datetime(year=2023, month=9, day=15, hour=2).hour
    if now not in range(sunrise, sunset + 1):
        # print('night')
        response = requests.get(url='http://api.open-notify.org/iss-now.json')
        response.raise_for_status()
        # print(response.json())
        data = response.json()['iss_position']
        longitude = int(float(data['longitude']))
        latitude = int(float(data['latitude']))
        # print(latitude, longitude)
        if LATITUDE in range(latitude - 5, latitude + 6) and LONGITUDE in range(longitude - 5, longitude + 6):
            # print('Look Up!!')
            with smtplib.SMTP('smtp.gmail.com', 587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=my_email,
                    msg='Subject:Hey!!\n\nLook Up!! There\'s ISS right above you!!'
                )
    # else:
    #     print('day')


#!/bin/python3
# Filename: lab_api-weather.py
# Course: Full Stack Developer Evening Bootcamps
# Author: Peter Chow and Drew, Students
# Assignment: Lab API: Weather API - Version 1
# Date: 10/21/2020
# Version 1.0

import requests
import json
import datetime
'''f4880b5dd2c51760b8ac4361e58abf6f'''
API_KEY = "de0486bfa33d259b7be3a5bf888cf0d4"
city = input("Ener a city for weather information: \n")
api_url = "https://api.openweathermap.org/data/2.5/weather?"
url = api_url + "q=" + city + "&units=imperial" + "&appid=" + API_KEY
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    main = data['main']
    temp = data['main']['temp']
    report = data['weather']
    date = data['dt']
    convert_date = datetime.datetime.utcfromtimestamp(date)
    print(f"{city:-^30}")
    print(
        f"Today's weather in {city} {report[0]['description']} {temp} |{convert_date}")
else:
    print(url)
    error = response.status_code
    print(f"Sorry, there seem to be an error.{error}")
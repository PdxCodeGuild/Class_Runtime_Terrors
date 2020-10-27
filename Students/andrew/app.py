import getpass
import smtplib
import tkinter as tk
import requests
import json
import datetime

HOST = "smtp.gmail.com"
PORT = "465"
BASEURL = "api.openweathermap.org/data/2.5/weather?zip="
API_KEY = "de0486bfa33d259b7be3a5bf888cf0d4"


default_user = "pythonweatherapp1@gmail.com"
to_address = "mlastof@gmail.com"
username = "pythonweatherapp1@gmail.com"
password = getpass.getpass("Enter gmail password")
zip_code = input("Ener a zipcode for your weather information: \n")
to_addr = input("Enter a recipiant")
server = smtplib.SMTP_SSL(HOST, PORT)
server.login(username, password)
weather_report = ""


def weather():
    api_url = "https://api.openweathermap.org/data/2.5/weather?"

    url = api_url + "zip=" + zip_code + "&units=imperial" + "&appid=" + API_KEY

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        main = data['main']
        temp = data['main']['temp']
        report = data['weather']
        date = data['dt']
        vis = data['visibility']
        convert_date = datetime.datetime.utcfromtimestamp(date)

        weather_msg = f"Today's weather in {zip_code} {report[0]['description']} {temp} |{convert_date} {vis}"
        return weather_msg
    else:
        print(url)
        error = response.status_code
        return "Sorry, there seem to be an error." + error


get_weather = weather()
#print(get_weather)
weather_report = get_weather.encode(encoding='UTF-8')
server.sendmail(
    default_user,
    to_addr,
    weather_report,
)
server.quit()

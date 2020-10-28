import requests
import getpass
import smtplib
from datetime import datetime, timedelta
from threading import Timer

HOST = "smtp.gmail.com"
PORT = 465

x=datetime.today()
y = x.replace(day=x.day, hour=21, minute=5, second=0, microsecond=0) + timedelta(days=1)
delta_t=y-x

secs=delta_t.total_seconds()

t = Timer(secs, weather_email)
t.start()

def weather():
    zip = input("What is the zip code you would like to check? : ")
    my_site = requests.get (f"http://api.openweathermap.org/data/2.5/weather?zip=97230,us&units=imperial&appid=f13b34adc98e544c0e9b823946d44c29")
    data = my_site.json()
    city = data["name"]
    temp = data["main"]["temp"]
    wind_speed = data["wind"]["speed"]

    if data["wind"]["deg"] >= 0 < 45 or data["wind"]["deg"] >= 315 <= 360:
        wind_dir = "North"
    elif data["wind"]["deg"] >= 45 < 135:
        wind_dir = "East"
    elif data["wind"]["deg"] >=135 < 225:
        wind_dir = "South"
    elif data["wind"]["deg"] >= 225 < 315:
        wind_dir = "West"

    return(f'''
In {city}, it is currently {temp} degrees.
The wind currently blowing {wind_dir} at {wind_speed} MPH.
''')
body = weather()

def weather_email():
    username = "cadillacjackproductions@gmail.com"
    password = getpass.getpass("Provide Gmail Password : ")
    server = smtplib.SMTP_SSL(HOST, PORT)

    server.login(username, password)

    server.sendmail(
        "cadillacjackproductions@gmail.com",
        "jamesdkeicher@gmail.com",
        "{}".format(body),
    )

    server.quit()
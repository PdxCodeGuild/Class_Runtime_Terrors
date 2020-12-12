import requests
import smtplib




HOST = "smtp.gmail.com"
PORT = 465
username = "cadillacjackproductions@gmail.com"
password = ""
server = smtplib.SMTP_SSL(HOST, PORT)

my_site = requests.get (f"http://api.openweathermap.org/data/2.5/weather?zip=97230,us&units=imperial&appid=f13b34adc98e544c0e9b823946d44c29")
data = my_site.json()
print(data)
city = data["name"]
temp = data["main"]["temp"]
temp_min = data["main"]["temp_min"]
temp_max = data["main"]["temp_max"]
wind_speed = data["wind"]["speed"]
wind_dir = data["wind"]["deg"]

content = f'''
The temperature in {city} is {temp} degrees.
The high for today is {temp_max} degrees.
The low for today is {temp_min} degrees.
The current winds are blowing at {wind_speed} MPH, at {wind_dir} degrees'''

server.login(username, password)
server.sendmail(
    f'{username}',
    'jamesdkeicher@gmail.com',
    "Subject:Portland Current Weather"
    f'{content}',
)
server.quit()


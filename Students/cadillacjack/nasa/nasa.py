import requests
import datetime
from PIL import Image as pic
from io import BytesIO
import smtplib
from random import randrange as new_day

HOST = "smtp.gmail.com"
PORT = 465
username = "cadillacjackproductions@gmail.com"
password = "462606Jk!$"
server = smtplib.SMTP_SSL(HOST, PORT)


today = datetime.date.today()

start_date = datetime.date(1995, 6, 16)

time_between = today - start_date
days_between = time_between.days
random_day = new_day(days_between)
random_day = start_date + datetime.timedelta(days = random_day)

my_site = requests.get (f"https://api.nasa.gov/planetary/apod?date={random_day}&api_key=4sGZ9oQpr4FqOaBewnmjODONv5FPIoOYB4dq6acz&hd=True")
data = my_site.json()

describe = data["explanation"]
hd_pic = data["hdurl"]
my_pic = requests.get(hd_pic)
pic_name = hd_pic[38:]
img = pic.open(BytesIO(my_pic.content))
img = img.save(f"/Users/cadillacjack/Desktop/API/APOD/{pic_name}")

server.login(username, password)
server.sendmail(
    f'{username}',
    'jamesdkeicher@gmail.com',
    'Subject:Apod'
    f'''
{describe}
{hd_pic}''',
)
server.quit()

print(describe)
print(hd_pic)

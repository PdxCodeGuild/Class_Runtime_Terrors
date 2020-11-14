import getpass
import smtplib

HOST = "smtp.gmail.com"
PORT = 465
username = "cadillacjackproductions@gmail.com"
password = "462606Jk!$"
server = smtplib.SMTP_SSL(HOST, PORT)

with open("weather.txt") as wet:
    wet = wet.read()

server.login(username, password)
server.sendmail(
    f'{username}',
    'jamesdkeicher@gmail.com',
    f'{wet}',
)
server.quit()
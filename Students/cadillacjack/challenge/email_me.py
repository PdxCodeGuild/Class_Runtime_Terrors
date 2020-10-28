import getpass
import smtplib
from crontab import CronTab

HOST = "smtp.gmail.com"
PORT = 465
username = "cadillacjackproductions@gmail.com"
password = getpass.getpass("Provide Gmail Password : ")
server = smtplib.SMTP_SSL(HOST, PORT)

server.login(username, password)

server.sendmail(
    "cadillacjackproductions@gmail.com",
    "jamesdkeicher@gmail.com",
    "{}".format,
)

server.quit()
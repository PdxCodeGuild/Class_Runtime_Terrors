# import smtplib, ssl

# port = 465  # For SSL
# smtp_server = "smtp.gmail.com"
# sender_email = "hotspotbrah@gmail.com"  # Enter your address
# receiver_email = "MrEricLe@gmail.com"  # Enter receiver address
# password = input("Type your password and press enter: ")
# message = """\
# Subject: Hi there

# This message is sent from Python."""

# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)

import smtplib

gmail_user = input('Your Email: ')
gmail_password = input("Your Password: ")

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo() #Like a Ping
    server.login(gmail_user, gmail_password)
except:
    print ('Something went wrong...')


sent_from = 'hotspotbrah@gmail.com'
to = 'mrericle@gmail.com'
subject = "OMG Super Important Message"
body ="Hey, what's up?\n\n- You"

email_text = "lol gets go"
From: 'mrericle@gmail.com'
To: 'mrericle@gmail.com'
Subject: 'Test'


try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print("Email sent!")
except:
    print("Something went wrong...")
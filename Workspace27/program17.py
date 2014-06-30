#sending email SMTPlib

import smtplib as mail

#Create smtp server connecion
mailServer = mail.SMTP("example.net")

#Login Credentials
mailServer.login("testuser","testpassword")

#Message Body
msg = '''From: Sender Name <sender@example.net>'
To: <reciepient@example.net>
Subject: A Test email message!
Content-type: text/html
MIME-Version:1.0

This will be the body of email'''

#Message headers (Content-type, MIME) are required if mail contains html and images otherwise message can be send directly as an argument in the sendmail method !

#object for sending mail
mailServer.sendmail("sender@example.net","reciepient@example.net",msg)


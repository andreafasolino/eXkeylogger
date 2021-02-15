import smtplib
from threading import Timer
from datetime import datetime


def sendmail(email, password, message):
    # connect to an SMTP server
    server = smtplib.SMTP(host="smtp.gmail.com", port=587)
    # connect to the SMTP server as TLS mode ( for security )
    server.starttls()
    # login to the email account
    server.login(email, password)
    # send the email
    server.sendmail(email, email, message)
    # terminates the session
    server.quit()


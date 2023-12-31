import smtplib, ssl
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

import os

username = os.getenv("MAIL_USERNAME")
password = os.getenv('PASSWORD')
host = os.getenv('HOST')
port = int(os.getenv('PORT'))


def send_email(message, receiver=None):
    if receiver is None:
        receiver = username
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(receiver, receiver, msg=message)
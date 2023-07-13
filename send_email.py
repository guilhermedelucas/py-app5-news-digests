import smtplib, ssl

with open('.env', 'r') as file:
    data = file.readlines()
    for line in data:
        key, info = line.strip().split('=')
        if key == 'USERNAME':
            username = info
        elif key == 'PASSWORD':
            password = info
        elif key == 'HOST':
            host = info
        elif key == 'PORT':
            port = info


def send_email(email, topic, message):
    receiver = username
    context = ssl.create_default_context()
    message = f"""\
Subject: New email from {email}

From: {email}
Topic {topic}
{message}
"""

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(receiver, receiver, msg=message)
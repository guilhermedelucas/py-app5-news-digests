import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

import os
from send_email import send_email

topic = "machine+AND+learning"
api_key = os.getenv("API_KEY")
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}" \
      "&sortBy=publishedAt" \
      f"&apiKey={api_key}" \
      "&language=pt"

# Make a description
request = requests.get(url)

# Make the description with data
content = request.json()

# Access the article titles and description
body = "Subject: Today's news \n"
for article in content['articles'][:20]:
    if article['title'] is not None:
        body = body + article['title'] + "\n" \
               + article['description'] + "\n" \
               + article['url'] + 2*"\n"

body = body.encode('utf-8')
send_email(message=body)
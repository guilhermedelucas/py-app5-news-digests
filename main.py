import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

import os

api_key = os.getenv("API_KEY")
print(api_key)
url = f"https://newsapi.org/v2/everything?q=tesla" \
      f"&from=2023-06-13&sortBy=publishedAt" \
      f"&apiKey={api_key}"

# Make a description
request = requests.get(url)

# Make the description with data
content = request.json()
print(content)

# Access the article titles and description
for article in content['articles']:
    print(article['title'])
    print(article['description'])
    print(article['url'])
import requests
import os

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

url = f"https://newsapi.org/v2/top-headlines?category=technology&language=en&pageSize=1&apiKey={NEWS_API_KEY}"

response = requests.get(url)
data = response.json()

article = data["articles"][0]

title = article["title"]
description = article["description"] or ""

with open("news.txt", "w", encoding="utf-8") as f:
    f.write(title + "\n")
    f.write(description)

print("News fetched")
from datetime import datetime
from slugify import slugify

with open("news.txt", "r", encoding="utf-8") as f:
    title = f.readline().strip()

slug = slugify(title)

date = datetime.now().strftime("%Y-%m-%d")

filename = f"articles/{date}-{slug}.md"

with open("article.md", "r", encoding="utf-8") as f:
    content = f.read()

with open(filename, "w", encoding="utf-8") as f:
    f.write(content)

print("Saved article")
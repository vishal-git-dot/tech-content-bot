import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

with open("news.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

title = lines[0].strip()
description = lines[1].strip()

prompt = f"""
Write a modern SEO-friendly tech article.

Title:
{title}

Description:
{description}

Requirements:
- 1000+ words
- Markdown format
- Human readable
- Professional style
- Use headings
"""

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

article = response.choices[0].message.content

with open("article.md", "w", encoding="utf-8") as f:
    f.write(article)

print("Article generated")
# API Setup Guide

This project uses:

- OpenAI API → for AI-generated articles
- NewsAPI → for fetching latest technology news

This guide explains how to create accounts, generate API keys, enable billing, and securely connect everything to GitHub Actions.

---

# Table of Contents

- What is an API?
- OpenAI API Setup
- NewsAPI Setup
- GitHub Secrets Setup
- Testing Your API Keys
- Common Errors
- Security Best Practices
- Cost & Free Tier Information

---

# What is an API?

An API (Application Programming Interface) allows your application to communicate with external services.

In this project:

```text
NewsAPI → Provides latest tech news
OpenAI API → Converts news into blog articles
```

Automation Flow:

```text
GitHub Actions
        ↓
Fetch News from NewsAPI
        ↓
Send news to OpenAI
        ↓
Generate AI article
        ↓
Save markdown file
        ↓
Push to GitHub repository
```

---

# OpenAI API Setup

Official Website:

https://platform.openai.com

---

## Step 1 — Create OpenAI Account

1. Visit:
   https://platform.openai.com/signup

2. Create account using:
   - Email
   - Google
   - Microsoft
   - Apple

3. Verify email.

---

## Step 2 — Open API Dashboard

Go to:

https://platform.openai.com

Dashboard includes:
- API Keys
- Usage
- Billing
- Projects
- Documentation

---

## Step 3 — Generate API Key

Open:

```text
Dashboard → API Keys
```

Or visit:

https://platform.openai.com/api-keys

Click:

```text
Create new secret key
```

Copy the generated key immediately.

Example:

```text
sk-proj-xxxxxxxxxxxxxxxx
```

IMPORTANT:
You can only see the full key once.

---

## Step 4 — Enable Billing

IMPORTANT:

ChatGPT subscription DOES NOT include API credits.

You must separately enable API billing.

Open:

https://platform.openai.com/settings/organization/billing

Add:
- Credit card
- Debit card

Recommended initial credits:
- $5
- $10

---

## Step 5 — Verify API Access

Go to:

```text
Dashboard → Usage
```

You should see:
- Requests
- Token usage
- Cost tracking

---

# Recommended OpenAI Models

| Model | Recommended | Cost |
|---|---|---|
| gpt-4.1-mini | YES | Cheap |
| gpt-4.1 | Optional | Higher |
| gpt-5 | Not needed initially | Expensive |

Recommended:

```python
model="gpt-4.1-mini"
```

---

# NewsAPI Setup

Official Website:

https://newsapi.org

---

## Step 1 — Create Account

Visit:

https://newsapi.org/register

Create free account.

---

## Step 2 — Get API Key

After login:

Open:
```text
Dashboard
```

Copy your API key.

Example:

```text
1234567890abcdef
```

---

## Step 3 — Understand Free Tier

Free tier includes:
- Developer usage
- Limited requests/day
- Great for learning projects

Perfect for:
- GitHub Actions automation
- Personal blogs
- Practice projects

---

# Example NewsAPI Request

```python
import requests

url = "https://newsapi.org/v2/top-headlines?category=technology&language=en&pageSize=1&apiKey=YOUR_API_KEY"

response = requests.get(url)

print(response.json())
```

---

# GitHub Secrets Setup

NEVER hardcode API keys inside your code.

BAD:

```python
OPENAI_API_KEY = "sk-xxxxx"
```

GOOD:

Use GitHub Secrets.

---

## Step 1 — Open Repository Settings

Go to:

```text
Repository → Settings
```

---

## Step 2 — Open Secrets

Navigate:

```text
Secrets and variables
→ Actions
```

---

## Step 3 — Add OpenAI Secret

Click:

```text
New repository secret
```

Add:

| Name | Value |
|---|---|
| OPENAI_API_KEY | Your OpenAI key |

---

## Step 4 — Add NewsAPI Secret

Add:

| Name | Value |
|---|---|
| NEWS_API_KEY | Your NewsAPI key |

---

# Using Secrets in GitHub Actions

Example:

```yaml
env:
  OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
  NEWS_API_KEY: ${{ secrets.NEWS_API_KEY }}
```

---

# Using Environment Variables in Python

Example:

```python
import os

api_key = os.getenv("OPENAI_API_KEY")
```

---

# Testing OpenAI API Locally

Example:

```python
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "user",
            "content": "Hello"
        }
    ]
)

print(response.choices[0].message.content)
```

---

# Testing NewsAPI Locally

Example:

```python
import requests
import os

api_key = os.getenv("NEWS_API_KEY")

url = f"https://newsapi.org/v2/top-headlines?category=technology&apiKey={api_key}"

response = requests.get(url)

print(response.json())
```

---

# Common Errors

---

## Error: insufficient_quota

Example:

```text
429 insufficient_quota
```

Cause:
- No billing
- No credits

Fix:
- Add payment method
- Add API credits

---

## Error: Invalid API Key

Cause:
- Wrong key
- Typo
- Deleted key

Fix:
- Generate new key
- Update GitHub Secret

---

## Error: Authentication Failed

Cause:
- Environment variable missing

Fix:
- Check GitHub Secrets
- Check variable names

---

## Error: Rate Limit

Cause:
- Too many requests

Fix:
- Reduce workflow frequency
- Upgrade API plan

---

# Security Best Practices

IMPORTANT:

Never:
- Commit API keys to GitHub
- Share screenshots of keys
- Store keys in public repos

Always:
- Use GitHub Secrets
- Rotate compromised keys
- Use environment variables

---

# Recommended Workflow

```text
GitHub Action
      ↓
Fetch latest news
      ↓
Generate AI article
      ↓
Save markdown file
      ↓
Push article to repository
```

---

# Cost Estimation

Using:

```python
gpt-4.1-mini
```

Approximate monthly cost:

| Articles/Day | Estimated Cost |
|---|---|
| 1 | Very low |
| 5 | Low |
| 20 | Moderate |

For beginners:
- $5 credits last a long time

---

# Useful Links

## OpenAI

- API Keys:
  https://platform.openai.com/api-keys

- Billing:
  https://platform.openai.com/settings/organization/billing

- Documentation:
  https://platform.openai.com/docs

---

## NewsAPI

- Official Website:
  https://newsapi.org

- Documentation:
  https://newsapi.org/docs

---

# Final Notes

This setup enables fully automated AI-generated blogging using:

- GitHub Actions
- Python
- OpenAI API
- NewsAPI

Once configured correctly, your repository can automatically:
- fetch technology news
- generate AI articles
- publish markdown content daily

with minimal manual work.

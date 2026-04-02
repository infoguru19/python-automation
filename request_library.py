# pip install requests

# 1. GET — Fetch / Read data
# Real-world analogy: Opening a webpage to read a blog post.

import requests

# Fetch a single post (post with id=1)
response = requests.get("https://api.github.com/users/lambda/subscriptions")

print(response.status_code)   # 200 means success
print(response.json())     # Convert response to Python dictionary


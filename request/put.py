import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts/1", verify=False)
data = response.json()
updated_post = {
    "id": 1,
    "title": "Updated Title",
    "body": "This content has been fully updated.",
    "userId": 1
}

response = requests.put(
    "https://jsonplaceholder.typicode.com/posts/1",  # update post with id=1
    json=updated_post,
    verify=False
)

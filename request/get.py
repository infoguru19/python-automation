
import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts/1", verify=False)
data = response.json()

# Status_code = 200 
print(response.status_code)
print(type(data))

print(data)
print(data["id"])

new_post = {
    "title": "My First Post",
    "body": "This is the content of my post.",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
     json=new_post,
     verify=False
)

print(response.status_code)   # 201 means "Created"
print(response.json())

updated_post = {
    "id": 1,
    "title": "Updated Title",
    "body": "This content has been fully updated.",
    "userId": 1
    headers = {
    "User-Agent": "Mozilla/5.0"
    }
}

response = requests.put(
    "https://jsonplaceholder.typicode.com/posts/1",  # update post with id=1
    json=updated_post,
    verify=False
)

print(response.status_code)   # 200 means success
print(response.json())


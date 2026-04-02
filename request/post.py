import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts/1", verify=False)
data = response.json()

new_post = {
    "title": "My First Post",
    "body": "This is the content of my post.",
    "userId": 1
}

response = requests.post( "https://jsonplaceholder.typicode.com/posts", json=new_post, verify=False )

print(response.status_code)   # 201 means "Created"
print(response.json())

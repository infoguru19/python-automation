import requests

url = 'https://api.github.com/users/lambda'
response = requests.get(url, verify=False)

print(response.status_code) # View the HTTP status code
# print(response.text)        # View the content as a string
my_data = response.json()
#print(response.json())
print(type(my_data))

repos = my_data.get("public_repos")
followers = my_data.get("followers")

total = repos + followers

print(f"total repos and followers: {total}")

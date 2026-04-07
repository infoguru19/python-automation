import json

with open("log", "r") as f:
    data = json.load(f)
    
demo = data[0]["protoPayload"]["serviceData"]["jobQueryResponse"]["job"]["jobStatus"]["error"]["message"]
print(demo)

# or 

for item in data:
   code = item["protoPayload"]["serviceData"]["jobQueryResponse"]["job"]["jobStatus"]["error"]["message"]
   print(code)

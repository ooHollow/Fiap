import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "Hello World",
    "body": "This is a test post",
    "userId": 1
}

response = requests.post(url, json=payload) #we change the get that we were using because now we wanna post something, and we specify the json because we learned that the second parameter is the params so it's better if we specify it

print("Stuatus code: ", response.status_code)
response.raise_for_status()

data = response.json()
print(data)
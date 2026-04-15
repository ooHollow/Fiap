import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print("Status Code: ", response.status_code)
print("Content: ", response.headers.get("Content-Type"))

data = response.json() #get all of the json data
print("Post title", data["title"])
import requests

url = "https://reqres.in/api/users"
params = {"page": 2}

response = requests.get(url, params)
print(f'Final url: {response.url}')

response.raise_for_status() #it stops the program if the status code is in between 4XX and 5XX

data = response.json()
print("Page", data["page"])
for user in data['data']:
    print(user["email"]) #it would return the page (page 2) and the emails in it, but it isn't working because I'm receiving status code 401
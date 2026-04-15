import requests

TOKEN = "TESTE"
url = "https://httpbin.org/post"

headers = {"Authorization": f"Bearer {TOKEN}"} #bearer 'e um tipo de autenticacao da api, vai mudar se mudar a api
response = requests.get(url, headers=headers)
response.raise_for_status()

print("URL: ", response.url)
print("Status code: ", response.status_code)

try:
    data = response.json()
    print(data)
except ValueError:
    print("Response is not JSON")
    print(response.text)
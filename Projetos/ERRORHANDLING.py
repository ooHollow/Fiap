import requests

url = "https://httpbin.org/delay/3"

try:
    response = requests.get(url, timeout=1)
    print(response.status_code)
    response.raise_for_status()
    print("Success", response.json())
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.RequestException as e:
    print(e)
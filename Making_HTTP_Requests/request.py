import requests

url = "https://www.typing.com/student/login"
url_2 = "https://www.google.com"

response = requests.get(url)
response_2 = requests.get(url_2)

print(f"Your request to {url} came back w/ status code {response.status_code}")
print(f"Your request to {url_2} came back w/ status code {response_2.status_code}")
import requests

TOKEN = "your_github_token"
headers = {"Authorization": f"token {TOKEN}"}

url = "https://api.github.com/user/repos"
payload = {"name": "TestRepo", "private": False}
response = requests.post(url, json=payload, headers=headers)

print(response.status_code)
print(response.json())

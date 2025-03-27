import requests

ENDPOINT = "https://api.github.com/users/pixegami"
response = requests.get(ENDPOINT)
data = response.json()

print(data["name"])
print(data["public_repos"])
print(data)
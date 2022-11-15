import requests

res = requests.get("https://ifconfig.me")

print(res.content)
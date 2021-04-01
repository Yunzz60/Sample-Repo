import requests

r = requests.get("https://www.berkeley.edu")
print(r.status_code)
print(r.ok)
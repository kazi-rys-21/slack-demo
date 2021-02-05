import requests
url = 'https://geek-jokes.sameerkumar.website/api'
response = requests.request("GET", url)
print(response.text)
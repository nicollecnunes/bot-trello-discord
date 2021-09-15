import requests
import json

#pega os membros em um card
url = "https://api.trello.com/1/cards/613b8700beff6540f4ba3f80/members"

response = requests.request(
"GET",
 url
  )

print(response.text)
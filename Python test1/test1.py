import requests
import json
from lostark_api_token import Token

headers = {
    'accept' : 'application/json',
    'authorization' : Token
}

url = 'https://developer-lostark.game.onstove.com/news/events'

response = requests.get(url, headers=headers)
jsonObject = response.json()

print(response)
print(jsonObject)

# cnt = 0
# json 출력 코드
# for list in jsonObject :
#     print(f"{cnt}번: ",list.get("Title"))
#     cnt += 1

# list로 출력 코드
jl = list()
for title in jsonObject :
    jsonObject = json.loads(response.text)

for i in range(len(jl)):
    print(f"{i}번: ",jl[i])

print(response.status_code)
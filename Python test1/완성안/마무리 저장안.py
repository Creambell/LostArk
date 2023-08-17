import requests
import json
import sys
from urllib import parse
from lostark_api_token import Token2
from lostark_api_token import Token3


def character_info_alert():
    string_original = input("캐릭터 이름 입력: ")
    string_encoded = parse.quote(string_original)
    

    try:
        headers = {
            'accept': 'application/json',
            'authorization': Token2,
        }
        url = 'https://developer-lostark.game.onstove.com/characters/' + string_encoded + '/siblings'
        response = requests.get(url, headers=headers)
        jsonObject = response.json()
        
        for list in jsonObject:
            print(list.get("ServerName"))
            print(list.get("CharacterName"))
            print(list.get("CharacterLevel"))
            print(list.get("CharacterClassName"))
            print(list.get("ItemAvgLevel"))
            print(list.get("ItemMaxLevel"))



    except TypeError:
        print("There is no character")



def character_image_alert():
    string_original = input("Type image    : ")
    string_encoded = parse.quote(string_original)
    headers = {
            'accept': 'application/json',
            'authorization': Token3,
        }
    url = 'https://developer-lostark.game.onstove.com/armories/characters/' + string_encoded + '/profiles'
    response = requests.get(url, headers=headers)
    jsonObject = response.json()

    if isinstance(jsonObject, dict):
        print(jsonObject.get("CharacterImage"))
        print(jsonObject.get("ExpeditionLevel"))
        print(jsonObject.get("PvpGradeName"))
        print(jsonObject.get("TownLevel"))
        print(jsonObject.get("TownName"))
        print(jsonObject.get("Title"))
        print(jsonObject.get("GuildMemberGrade"))
        print(jsonObject.get("GuildName"))
        print(jsonObject.get("UsingSkillPoint"))
        print(jsonObject.get("TotalSkillPoint"))
    else:
        print("X")
    
def print_menu():
        print("1. 캐릭터 정보")
        print("2. 캐릭터 이미지")
        print("3. out")
        
        inputed_number = int(input("번호를 입력해주세요 :"))
        return inputed_number
        
while True :
    inputed_number = print_menu()
    
    if inputed_number == 1:
        character_info_alert()
    elif inputed_number == 2:
        character_image_alert()
    elif inputed_number == 3:
        print("out 실행")

    else:
        print("다시 입력해주세요")
        break

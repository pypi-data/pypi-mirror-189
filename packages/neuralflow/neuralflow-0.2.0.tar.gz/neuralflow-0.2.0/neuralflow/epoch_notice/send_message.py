import requests
import json

# 발행한 토큰 불러오기
with open("./token.json", "r") as kakao:
    tokens = json.load(kakao)

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

headers = {
    "Authorization": "Bearer " + tokens["access_token"]
}

data = {
    'object_type': 'text',
    'text': '1epoch 종료',
    'link': {
        'web_url': 'https://developers.kakao.com',
        'mobile_web_url': 'https://developers.kakao.com'
    },
    'button_title': 'epoch alert'
}


data = {'template_object': json.dumps(data)}
response = requests.post(url, headers=headers, data=data)
print(response.status_code)
print(response.text)


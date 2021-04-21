import requests, uuid

#channel id: 1627632136

headers = {
    "Content-Type": "application/json",
    "X-Line-Translate-From": "line_camera",
    "X-Line-ChannelToken": "your_channel_token"
    }

djson = {
    "tLang": "id",
    "id": str(uuid.uuid4()),
    "originalText": "how are you",
    "sLang": "en"
    }

r = requests.post("https://gw.line.naver.jp/ds/translate/translate/legyTransAPI.nhn",headers=headers,json=djson).json(0
print(r)


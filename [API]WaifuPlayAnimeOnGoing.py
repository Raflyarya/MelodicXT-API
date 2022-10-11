import requests,json


def WaifuplayOngoing_execute():
    url = requests.get("https://melodicxt-simple.herokuapp.com/api/anime/waifuplay-ongoing")
    info = url.text
    data = json.loads(info)
    return (json.dumps(data,indent=4,ensure_ascii=False))

a = WaifuplayOngoing_execute()
print(a)
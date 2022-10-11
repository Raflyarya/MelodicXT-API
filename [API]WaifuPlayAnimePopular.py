import requests,json


def WaifuplayPopularAnime_execute():
    url = requests.get("https://melodicxt-simple.herokuapp.com/api/anime/waifuplay-popular-anime")
    info = url.text
    data = json.loads(info)
    return (json.dumps(data,indent=4,ensure_ascii=False))

a = WaifuplayPopularAnime_execute()
print(a)
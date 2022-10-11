import requests,json


def WaifuplaySearchAnime_execute(query):
    url = requests.get("https://melodicxt-simple.herokuapp.com/api/anime/waifuplay-search-anime?query={}".format(query))
    info = url.text
    data = json.loads(info)
    return (json.dumps(data,indent=4,ensure_ascii=False))

a = WaifuplaySearchAnime_execute('isekai')
print(a)

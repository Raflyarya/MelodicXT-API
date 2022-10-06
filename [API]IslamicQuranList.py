import requests,json


def IslamicQuranListSurah_execute():
    url = requests.get("https://melodicxt-simple.herokuapp.com/api/islamic/quranlistsurah")
    info = url.text
    data = json.loads(info)
    return (json.dumps(data,indent=4,ensure_ascii=False))

a = IslamicQuranListSurah_execute()
print(a)
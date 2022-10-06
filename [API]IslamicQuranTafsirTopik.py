import requests,json


def IslamicQuranTafsirTopik_execute(query):
    url = requests.get("https://melodicxt-simple.herokuapp.com/api/islamic/qurantafsirtopik?query={}".format(query))
    info = url.text
    data = json.loads(info)
    return (json.dumps(data,indent=4,ensure_ascii=False))

a = IslamicQuranTafsirTopik_execute('dajal')
print(a)
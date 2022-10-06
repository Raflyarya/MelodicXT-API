import requests,json


def IslamicQuranSurahByNumber_execute(number):
    url = requests.get("https://melodicxt-simple.herokuapp.com/api/islamic/quransurahbynumber?number={}".format(number))
    info = url.text
    data = json.loads(info)
    return (json.dumps(data,indent=4,ensure_ascii=False))

a = IslamicQuranSurahByNumber_execute('1')
print(a)
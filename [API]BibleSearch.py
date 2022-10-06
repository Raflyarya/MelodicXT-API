import requests,json


def BibleSearch_execute(query):
    url = requests.get("https://melodicxt-simple.herokuapp.com/api/bible/search?query={}".format(query))
    info = url.text
    data = json.loads(info)
    return (json.dumps(data,indent=4,ensure_ascii=False))

a = BibleSearch_execute('yesus')
print(a)
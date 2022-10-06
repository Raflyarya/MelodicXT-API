import requests,json


def HalodocSearchBidan_execute(query):
    url = requests.get("https://melodicxt-simple.herokuapp.com/api/halodoc/search-bidan?query={}".format(query))
    info = url.text
    data = json.loads(info)
    return (json.dumps(data,indent=4,ensure_ascii=False))

a = HalodocSearchBidan_execute('rika')
print(a)
import requests,json


def HalodocSearchDoctor_execute(query):
    url = requests.get("https://melodicxt-simple.herokuapp.com/api/halodoc/search-dokter?query={}".format(query))
    info = url.text
    data = json.loads(info)
    return (json.dumps(data,indent=4,ensure_ascii=False))

a = HalodocSearchDoctor_execute('udin')
print(a)
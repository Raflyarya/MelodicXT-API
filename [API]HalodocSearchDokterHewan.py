import requests,json


def HalodocSearchDokterHewan_execute(query):
    url = requests.get("https://melodicxt-simple.herokuapp.com/api/halodoc/search-dokter-hewan?query={}".format(query))
    info = url.text
    data = json.loads(info)
    return (json.dumps(data,indent=4,ensure_ascii=False))

a = HalodocSearchDokterHewan_execute('ari')
print(a)
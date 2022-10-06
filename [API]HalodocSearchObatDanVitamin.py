import requests,json


def HalodocSearchObatDanVitamin_execute(query):
    url = requests.get("https://melodicxt-simple.herokuapp.com/api/halodoc/search-obat-dan-vitamin?query={}".format(query))
    info = url.text
    data = json.loads(info)
    return (json.dumps(data,indent=4,ensure_ascii=False))

a = HalodocSearchObatDanVitamin_execute('obat batuk')
print(a)
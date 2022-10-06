import requests,json


def LowonganKerjaBySearch_execute(query):
    url = requests.get("https://melodicxt-simple.herokuapp.com/api/LowonganKerja/bysearch?location={}".format(query))
    info = url.text
    data = json.loads(info)
    return (json.dumps(data,indent=4,ensure_ascii=False))

a = LowonganKerjaBySearch_execute()
print(a)
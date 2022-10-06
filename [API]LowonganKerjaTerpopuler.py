import requests,json


def LowonganKerjaTerpopuler_execute():
    url = requests.get("https://melodicxt-simple.herokuapp.com/api/LowonganKerja/terpopuler")
    info = url.text
    data = json.loads(info)
    return (json.dumps(data,indent=4,ensure_ascii=False))

a = LowonganKerjaTerpopuler_execute()
print(a)
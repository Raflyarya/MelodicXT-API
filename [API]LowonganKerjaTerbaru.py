import requests,json


def LowonganKerjaTerbaru_execute():
    url = requests.get("https://melodicxt-simple.herokuapp.com/api/LowonganKerja/terbaru")
    info = url.text
    data = json.loads(info)
    return (json.dumps(data,indent=4,ensure_ascii=False))

a = LowonganKerjaTerbaru_execute()
print(a)
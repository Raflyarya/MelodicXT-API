import requests,json


def LowonganKerjaByLocation_execute(location):
    url = requests.get("https://melodicxt-simple.herokuapp.com/api/LowonganKerja/bylocation?location={}".format(location))
    info = url.text
    data = json.loads(info)
    return (json.dumps(data,indent=4,ensure_ascii=False))

a = LowonganKerjaByLocation_execute('jakarta')
print(a)
import requests,json


def MIslamicMasehiToHijriah_execute(day,month,year):
    url = requests.get("https://melodicxt-simple.herokuapp.com/api/islamic/masehitohijriah?day={}&month={}&year={}".format(day,month,year))
    info = url.text
    data = json.loads(info)
    return (json.dumps(data,indent=4,ensure_ascii=False))

a = MIslamicMasehiToHijriah_execute('1','10','2022')
print(a)
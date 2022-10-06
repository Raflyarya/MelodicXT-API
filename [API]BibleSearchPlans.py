import requests,json


def BibleSearchPlans_execute(query):
    url = requests.get("https://melodicxt-simple.herokuapp.com/api/bible/searchplans?query={}".format(query))
    info = url.text
    data = json.loads(info)
    return (json.dumps(data,indent=4,ensure_ascii=False))

a = BibleSearchPlans_execute('beristirahat')
print(a)
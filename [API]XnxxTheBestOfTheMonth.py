import requests,json


def XnxxTheBestOfTheMonth_execute():
    url = requests.get("https://melodicxt-simple.herokuapp.com/api/xnxx/the-best-of-the-month")
    info = url.text
    data = json.loads(info)
    return (json.dumps(data,indent=4,ensure_ascii=False))

a = XnxxTheBestOfTheMonth_execute()
print(a)

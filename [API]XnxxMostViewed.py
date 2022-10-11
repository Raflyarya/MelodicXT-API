import requests,json


def XnxxMostViewed_execute():
    url = requests.get("https://melodicxt-simple.herokuapp.com/api/xnxx/most-viewed")
    info = url.text
    data = json.loads(info)
    return (json.dumps(data,indent=4,ensure_ascii=False))

a = XnxxMostViewed_execute()
print(a)

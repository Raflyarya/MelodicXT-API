import requests,json


def XnxxSearch_execute(query):
    url = requests.get("https://melodicxt-simple.herokuapp.com/api/xnxx/search?query={}".format(query))
    info = url.text
    data = json.loads(info)
    return (json.dumps(data,indent=4,ensure_ascii=False))

a = XnxxSearch_execute('gisel')
print(a)

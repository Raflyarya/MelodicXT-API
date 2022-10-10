import requests,json


def WikimediaSearchVideo_execute(query):
    url = requests.get("https://melodicxt-simple.herokuapp.com/api/wikimedia/search-video?query={}".format(query))
    info = url.text
    data = json.loads(info)
    return (json.dumps(data,indent=4,ensure_ascii=False))

a = WikimediaSearchVideo_execute('jokowi')
print(a)
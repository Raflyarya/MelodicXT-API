import requests,json


def WikimediaSearchImage_execute(query):
    url = requests.get("https://melodicxt-simple.herokuapp.com/api/wikimedia/search-image?query={}".format(query))
    info = url.text
    data = json.loads(info)
    return (json.dumps(data,indent=4,ensure_ascii=False))

a = WikimediaSearchImage_execute('jokowi')
print(a)

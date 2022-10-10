import requests,json


def WikimediaSearchArticle_execute(query):
    url = requests.get("https://melodicxt-simple.herokuapp.com/api/wikimedia/search-article?query={}".format(query))
    info = url.text
    data = json.loads(info)
    return (json.dumps(data,indent=4,ensure_ascii=False))

a = WikimediaSearchArticle_execute('jokowi')
print(a)

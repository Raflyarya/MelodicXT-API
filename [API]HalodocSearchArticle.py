import requests,json


def HalodocSearchArticle_execute(query):
    url = requests.get("https://melodicxt-simple.herokuapp.com/api/halodoc/search-article?query={}".format(query))
    info = url.text
    data = json.loads(info)
    return (json.dumps(data,indent=4,ensure_ascii=False))

a = HalodocSearchArticle_execute('covid')
print(a)
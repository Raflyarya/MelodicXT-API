import requests,json


def MovieSearchToWatch_execute(query):
    url = requests.get("https://melodicxt-simple.herokuapp.com/api/movie/searchtowatch?query={}".format(query))
    info = url.text
    data = json.loads(info)
    return (json.dumps(data,indent=4,ensure_ascii=False))

a = MovieSearchToWatch_execute('joker')
print(a)
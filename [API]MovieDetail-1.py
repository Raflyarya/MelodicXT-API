import requests,json


def MovieInfoDetail1_execute(query):
    url = requests.get("https://melodicxt-simple.herokuapp.com/api/movie/infodetail-1?query={}".format(query))
    info = url.text
    data = json.loads(info)
    return (json.dumps(data,indent=4,ensure_ascii=False))

a = MovieInfoDetail1_execute('doraemon')
print(a)
import requests,json


def MovieInfoDetail2_execute(query,year):
    url = requests.get("https://melodicxt-simple.herokuapp.com/api/movie/infodetail-2?query={}&year={}".format(query,year))
    info = url.text
    data = json.loads(info)
    return (json.dumps(data,indent=4,ensure_ascii=False))

a = MovieInfoDetail2_execute('doraemon','2017')
print(a)
import requests,json


def MovieSuggestion_execute_execute():
    url = requests.get("https://melodicxt-simple.herokuapp.com/api/movie/suggestion")
    info = url.text
    data = json.loads(info)
    return (json.dumps(data,indent=4,ensure_ascii=False))

a = MovieSuggestion_execute_execute()
print(a)
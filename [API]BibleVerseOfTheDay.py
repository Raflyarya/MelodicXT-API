import requests,json


def BibleVerseOfTheDay_execute():
    url = requests.get("https://melodicxt-simple.herokuapp.com/api/bible/verseoftheday")
    info = url.text
    data = json.loads(info)
    return (json.dumps(data,indent=4,ensure_ascii=False))

a = BibleVerseOfTheDay_execute()
print(a)
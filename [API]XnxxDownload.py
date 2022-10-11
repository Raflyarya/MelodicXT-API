import requests,json


def XnxxDownload_execute(url):
    url = requests.get("https://melodicxt-simple.herokuapp.com/api/xnxx/download?url={}".format(url))
    info = url.text
    data = json.loads(info)
    return (json.dumps(data,indent=4,ensure_ascii=False))

a = XnxxDownload_execute('https://www.xnxx.com/video-w8qxfcf/giselle_montes_riding_hard')
print(a)

import requests

url = "http://localhost:1337/v2/carindex"
# url = "https://7d24-190-166-177-68.ngrok.io/v2/carindex"



def laraIndex(item):
    req = requests.post(url, json = item )
    print(req.text)


def soldItem(item):
    body = {
        "uid": item
    }
    req = requests.post('http://localhost:1337/carindex/marksold', json = body)
    print(req.text)
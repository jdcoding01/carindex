import requests

url = "https://lara.barrancosecurity.me/v2/carindex"
# url = "https://7d24-190-166-177-68.ngrok.io/v2/carindex"



def laraIndex(item):
    req = requests.post(url, json = item )
    print(req.text)
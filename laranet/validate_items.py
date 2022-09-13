import requests
import bs4 as bs

# Checks for sold items
def soldItem(item):
    body = {
        "uid": item
    }
    req = requests.post('http://localhost:1337/carindex/marksold', json = body)
    print(req.text)

    
uids = requests.get("https://lara.barrancosecurity.me/carindex/uids")

j = uids.json()
itemCount = len(j['data'])
count = len(j['data'])

for item in j['data']:
    itemCount = itemCount - 1
    uid = item["uid"]

    source = requests.get(url=
"https://www.encuentra24.com/panama-es/searchresult/autos?q=f_make.|keyword.{}".format(uid))
    soup = bs.BeautifulSoup(source.text, "html.parser")



    found = soup.find("div", {"class": "col-xs-12"})


    if found is not None:
        soldItem(uid)
    else:
        print('available -> {}/{}'.format(itemCount, count))

from helpers.http_manager import soldItem





# Checks for sold items

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
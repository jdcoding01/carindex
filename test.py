import string
import bs4 as bs
import requests
import time
from datetime import datetime
import threading
import sys


# source = requests.get(url=
# "https://www.encuentra24.com/panama-es/searchresult/autos?q=f_make.")
# soup = bs.BeautifulSoup(source.text, "html.parser")

# items = soup.find("div", {"class": "ann-subcat-listing"})


# articles = items.find_all("article", {"class": "ann-box-teaser"})

# for item in articles:
#     a = item.find("div", {"class": "ann-box-details"})
#     url = a.find("a", {"class": "more-details"})
#     url_parsed = str(url).split("href=")[1].split('"')[1]
#     if url_parsed != "/panama-es/bluebook":
#         print(str(url).split("href=")[1].split('"')[1])


listt = [
    "localizacion",
    "marca",
    "modelo",
    "fecha_publicacion",
    "precio",
    "year",
    "km",
    "transmision",
    "combustible",
    "vendedor",
    "phone" ]

for i in listt:
    print("\"{}\": {},".format(i, i))

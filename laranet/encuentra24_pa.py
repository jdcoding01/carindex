import bs4 as bs
import requests
import math
from datetime import date

from datetime import datetime as dt
from halo import Halo
import time
import requests

url = "http://localhost:1337/v2/carindex"


def laraIndex(item):
    req = requests.post(url, json=item)
    print(req.text)


class Encuentra24Interface:
    def __init__(self, url, max_items, items_per_page, config, usd_conversion_rate):
        self.url = url
        self.max_items = max_items
        self.items_per_page = items_per_page
        self.config = config
        self.usd_conversion_rate = usd_conversion_rate

    # Find all items on each page, based on max_items provided
    def read_items_by_page(self):
        print("Called")
        max_pages = math.floor(self.max_items / self.items_per_page)
        current_page = 1
        parsed_items = 0

        while current_page <= max_pages:
            source = requests.get(
                url="https://www.encuentra24.com/panama-es/searchresult/autos.{}?q=f_make.".format(
                    current_page
                )
            )

            soup = bs.BeautifulSoup(source.text, "html.parser")

            items = soup.find("div", {"class": "ann-subcat-listing"})

            articles = items.find_all("article", {"class": "ann-box-teaser"})

            for item in articles:
                a = item.find("div", {"class": "ann-box-details"})
                url = a.find("a", {"class": "more-details"})
                url_parsed = str(url).split("href=")[1].split('"')[1]
                if url_parsed != "/panama-es/bluebook":

                    parsed_items += 1
                    self.load_item_data(self.url, url_parsed, parsed_items)

                    print(
                        "\r"
                        + "[Encuentra24]: "
                        + str(round(parsed_items / self.max_items * 100, 1))
                        + "% complete"
                        + " ({}/{}) items captured.".format(
                            parsed_items, self.max_items
                        ),
                        end="",
                    )

                    with open('./scans/scan-{}.txt'.format(date.today()), "w") as scan:
                        scan.write("{}".format(parsed_items))
                        scan.close()

                if parsed_items == self.max_items:
                    print("max")
                    break
            current_page += 1

    # Captures data for a specific entry/item with provided url
    def load_item_data(self, url, path, count):
        item_url = "{}{}".format(url, path)
        source = requests.get(url=item_url)

        soup = bs.BeautifulSoup(source.text, "html.parser")
        ad_info = soup.find_all("div", {"class": "ad-info"})
        ad_details = soup.find_all("div", {"class": "ad-details"})
        user_info = soup.find("div", {"class": "user-info"})

        try:
            uid = item_url.split("?q=")[0].split("/")[7]
        except IndexError:
            uid = "none"

        localizacion = ""
        marca = ""
        modelo = ""
        fecha_publicacion = ""
        precio = 0
        year = 0
        km = 0
        transmision = ""
        combustible = ""

        vendedor = ""
        phone = ""
        financiamiento = soup.find("a", {"class": "funding"})

        if financiamiento is not None:
            financiamiento = "si"
        else:
            financiamiento = "no"

        try:
            localizacion = (
                str(ad_info[0].find_all("li")[0].find_all("span")[1])
                .split(">")[1]
                .split("</")[0]
            )
            marca = (
                str(ad_info[0].find_all("li")[1].find_all("span")[1])
                .split(">")[1]
                .split("</")[0]
            )
            modelo = (
                str(ad_info[0].find_all("li")[2].find_all("span")[1])
                .split(">")[1]
                .split("</")[0]
            )
            fecha_publicacion = (
                str(ad_info[0].find_all("li")[3].find_all("span")[1])
                .split(">")[1]
                .split("</")[0]
            )
            precio = (
                str(ad_info[0].find_all("li")[4].find_all("span")[1])
                .split(">")[1]
                .split("</")[0]
                .split(".00")[0]
            )
            year = (
                str(ad_details[0].find_all("li")[0])
                .split('info-value">')[1]
                .split("</span>")[0]
            )
            km = (
                str(ad_details[0].find_all("li")[1])
                .split('info-value">')[1]
                .split("</span>")[0]
            )
            transmision = (
                str(ad_details[0].find_all("li")[2])
                .split('info-value">')[1]
                .split("</span>")[0]
            )
            combustible = (
                str(ad_details[0].find_all("li")[3])
                .split('info-value">')[1]
                .split("</span>")[0]
            )

            vendedor = (
                str(user_info.find("span", {"class": "user-name"}))
                .split('">')[1]
                .split("</span>")[0]
            )

            phone = ""

        except IndexError:
            pass

        print(
            "{} - {} - {} - {} - ${} - {} - km {} - {} - {} - sold by: {} call at: ({})".format(
                localizacion,
                marca,
                modelo,
                year,
                str(precio).split(".00")[0],
                fecha_publicacion,
                km,
                transmision,
                combustible,
                vendedor,
                phone,
            )
        )

        param_value_getter = {
            "eventType": "index_item",
            "localizacion": localizacion,
            "marca": marca,
            "modelo": modelo,
            "fecha_publicacion": fecha_publicacion,
            "precio": precio,
            "year": year,
            "km": km,
            "transmision": transmision,
            "combustible": combustible,
            "vendedor": vendedor,
            "phone": phone,
            "uid": uid,
            "financiamiento": str(financiamiento),
            "module": "encuentra24-pa",
        }

        #laraIndex(param_value_getter)

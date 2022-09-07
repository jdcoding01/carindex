import json
from helpers.config_generator import ConfigGenerator
from sites.encuentra24.encuentra24 import Encuentra24Interface
from sites.encuentra24_cr.encuentra24_cr import Encuentra24CrInterface


# Configuration file for script
config_file = "config.json"


class SiteScraper:
    def __init__(self):
        with open(config_file, "r") as main_config:
            data = json.load(main_config)

            # Iterates over the specified enabled sites and calls the corresponding handler
            for i in data["sites"]:           
                if i["identifier"] == "encuentra24":
                    ConfigGenerator(
                        i["identifier"],
                        i["baseUrl"],
                        i["max_items"],
                        i["items_per_page"],
                        i["defaults"],
                        i["usd_conversion_rate"]
                    ).generate_config()

                    with open(i["config"], "r") as config:
                        contents = json.load(config)
                        try:

                            Encuentra24Interface(
                                contents["url"],
                                contents["max_items"],
                                contents["items_per_page"],
                                contents["enabled_params"],
                                contents["usd_conversion_rate"]
                            ).read_items_by_page()
                            config.close()
                        except KeyboardInterrupt:
                            print("Ecuentra24 finished!")
                  
                
                if i["identifier"] == "encuentra24_cr":
                    ConfigGenerator(
                        i["identifier"],
                        i["baseUrl"],
                        i["max_items"],
                        i["items_per_page"],
                        i["defaults"],
                        i["usd_conversion_rate"]
                    ).generate_config()

                    with open(i["config"], "r") as config:
                        contents = json.load(config)
                        try:

                            Encuentra24CrInterface(
                                contents["url"],
                                contents["max_items"],
                                contents["items_per_page"],
                                contents["enabled_params"],
                                contents["usd_conversion_rate"]
                            ).read_items_by_page()
                            config.close()
                        except KeyboardInterrupt:
                            print("Ecuentra24 Costa Rica finished!")


            main_config.close()


SiteScraper()
import json
import sys

class ConfigGenerator:
    def __init__(self, module, url, max_items, items_per_page, supercasas_item_properties, usd_conversion_rate):
        self.module = module
        self.url = url
        self.max_items = max_items
        self.items_per_page = items_per_page
        self.supercasas_item_properties = supercasas_item_properties
        self.usd_conversion_rate = usd_conversion_rate

    # Writes module-specific config to JSON file
    def write_config(self, data):
        with open("./sites/{}/config.json".format(self.module), "w+") as config:
            config.write(json.dumps(data))
            config.close()

    # Generates config.json for "Supercasas.com" module based on project's main_config JSON file
    def generate_supercasas_config(self):
        enabled_item_properties = []

        config_body = {
            "identifier": self.module,
            "url": self.url,
            "max_items": self.max_items,
            "items_per_page": self.items_per_page,
            "available_params": [],
            "enabled_params": enabled_item_properties,
            "usd_conversion_rate": self.usd_conversion_rate
        }

        for item_property in self.supercasas_item_properties:
            identifier = item_property.split(":")[0].replace(" ", "-").lower()
            name = item_property.split(":")[0]
            enabled = item_property.split(":")[2]

            enabled_item_property_body = {"identifier": identifier, "name": name, "enabled": enabled}

            enabled_item_properties.append(enabled_item_property_body)

        self.write_config(config_body)

    # Identifies provided module and assigns corresponding handler
    def generate_config(self):
        options = {"encuentra24": self.generate_supercasas_config, "encuentra24_cr": self.generate_supercasas_config}

        options[self.module]()

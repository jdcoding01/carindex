from encuentra24_pa import Encuentra24Interface

enabled_params = [
    {"identifier": "localizacion", "name": "localizacion", "enabled": "true"},
    {"identifier": "marca", "name": "marca", "enabled": "true"},
    {"identifier": "modelo", "name": "modelo", "enabled": "true"},
    {"identifier": "fecha_publicacion", "name": "fecha_publicacion", "enabled": "true"},
    {"identifier": "precio", "name": "precio", "enabled": "true"},
    {"identifier": "year", "name": "year", "enabled": "true"},
    {"identifier": "km", "name": "km", "enabled": "true"},
    {"identifier": "transmision", "name": "transmision", "enabled": "true"},
    {"identifier": "combustible", "name": "combustible", "enabled": "true"},
    {"identifier": "vendedor", "name": "vendedor", "enabled": "true"},
    {"identifier": "phone", "name": "phone", "enabled": "true"},
    {"identifier": "uid", "name": "uid", "enabled": "true"},
    {"identifier": "financiamiento", "name": "financiamiento", "enabled": "true"},
]


def scanner(module):  
    print("started") 
    workers = {
        "encuentra24-pa": Encuentra24Interface(
            "https://www.encuentra24.com/", 30, 15, enabled_params, 55
        ).read_items_by_page()
    }

    workers[module]




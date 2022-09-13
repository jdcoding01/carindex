import requests
import statistics

url = "http://localhost:1337/all_items"

req = requests.get(url)
dataset = req.json()['data']

def totalItems():
    sold = []
    for item in dataset:
        if item["unavailable_timestamp"] is not None:
            sold.append(item)
    return {
        "total": len(dataset),
        "sold": len(sold),
        "available": len(dataset) - len(sold)
    }

def logger(entry):
    with open("./checklist.txt", "a") as checklist:
        checklist.write(entry)
        checklist.write("/n")
        checklist.close()

def laraIndex():
    req = requests.get(url)
    dataset = req.json()['data']

    prices = []

    for entry in dataset:
        try:
            try:
                prices.append(int(entry['precio'].split('B/.')[1].replace(',', '')))
            except ValueError:
                prices.append(int(entry['precio'].split('B/.')[1].replace(',', '').split('.')[0]))
        except IndexError:
            logger(entry["uid"])

    print(round(statistics.mean(prices)))


# Most indexed brands
def getTopBrands(number):
    brands = []
    sorted_brands_list = []

    for item in dataset:
        brands.append(item['marca'])
    
    counts = { brand:brands.count(brand) for brand in brands}
    sorted_brands = {k: v for k, v in sorted(counts.items(), reverse=True, key=lambda item: item[1])}
    
    for key in sorted_brands:
        sorted_brands_list.append({ "name": "{} - {}".format(sorted_brands[key], key), "value": sorted_brands[key], "id": key})
    
    return sorted_brands_list[:number]


# Returns most sold brands
def mostSoldBrands(number):
    brands = []
    sorted_brands_list = []

    for item in dataset:
        if item['unavailable_timestamp'] is not None:
            print("{} - {}".format(item['uid'], item['marca']))
            brands.append(item['marca'])
    
    counts = { brand:brands.count(brand) for brand in brands}
    sorted_brands = {k: v for k, v in sorted(counts.items(), reverse=True, key=lambda item: item[1])}
    
    for key in sorted_brands:
        sorted_brands_list.append({ "brand": key, "count": sorted_brands[key]})
    
    print(sorted_brands_list[:number])


# Most sold model by Brand
def mostSoldBrandModel(number, brand):
    brands = []
    sorted_brands_list = []

    for item in dataset:
        if item['unavailable_timestamp'] is not None and item['marca'] == brand:

            brands.append("{} {}".format(item['modelo'], item['year']))
    
    counts = { brand:brands.count(brand) for brand in brands}
    sorted_brands = {k: v for k, v in sorted(counts.items(), reverse=True, key=lambda item: item[1])}
    
    for key in sorted_brands:
        sorted_brands_list.append({ "brand": key, "count": sorted_brands[key]})
    
    print(sorted_brands_list[:5])

# Most sold model by Brand and Year
def mostSoldBrandModelByYear(number, brand, year):
    brands = []
    sorted_brands_list = []

    for item in dataset:
        if item['unavailable_timestamp'] is not None and item['marca'] == brand and item['year'] == year:
            brands.append("{} {}".format(item['modelo'], item['year']))
    
    counts = { brand:brands.count(brand) for brand in brands}
    sorted_brands = {k: v for k, v in sorted(counts.items(), reverse=True, key=lambda item: item[1])}
    
    for key in sorted_brands:
        sorted_brands_list.append({ "brand": key, "count": sorted_brands[key]})
    
    print(sorted_brands_list[:5])


def averagePrice(brand, model, year):
    prices = []

    for item in dataset:
        if item["marca"] == brand and item["modelo"] == model and item["year"] == year:
            try:
                try:
                    prices.append(int(item['precio'].split('B/.')[1].replace(',', '')))
                except ValueError:
                    prices.append(int(item['precio'].split('B/.')[1].replace(',', '').split('.')[0]))
            except IndexError:
                logger(item["uid"])
    print(round(statistics.mean(prices)))




 # Cual es el modelo mas vendido en toyota? -
 # Cual es el modelo mas vendido en toyota 2015? -
 # Cual es el precio promedio de un toyota corolla 2015?  -



# precio promedio: brand model year fuel
# modelo mas vendido: brand year

modules = [
    "preciopromedio",
    "modelomasvendido"
]

def performTask(intent, query):
    moduleTree = {
        "preciopromedio": averagePrice(query[0], query[1], query[2])
    }

def manager(query):
    intent = query.split(":")[0].replace(" ", "")
    task = query.split(":")[1].strip().split(" ")

    if intent in modules:
        performTask(intent, task)
    else :
        print(intent + " not found.")



def getPriceAverage(brand):
    prices = []

    for item in dataset:
        if item["marca"] == brand:
            try:
                try:
                    prices.append(int(item['precio'].split('B/.')[1].replace(',', '')))
                except ValueError:
                    prices.append(int(item['precio'].split('B/.')[1].replace(',', '').split('.')[0]))
            except IndexError:
                logger(item["uid"])
    return round(statistics.mean(prices))


def getTopBrandsPriceAverage():
    brands = getTopBrands(5)
    averages = []

    for item in brands:

        average = getPriceAverage(item['id'])
        averages.append({ "brand": item['name'], "average": average})
    print(averages)
    return averages


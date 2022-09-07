from statistics import mean 
from database_manager import DatabaseManager
import os 
import locale


def getMostPopular():
    labels = DatabaseManager("encuentra24").count_make()
    marcas = []


    labels.sort(key = lambda labels: labels[1], reverse= True)

    for item in labels:
        marcas.append({ "name": "{} - {}".format(item[1], item[0]), "value": item[1], "key": item[0] })

    return marcas[:10]

def getReports():
    reports = []
    files = os.listdir("/Users/jose/dev/car_indexing/reports/encuentra24")

    for file in files:
        if file.endswith(".xlsx"):
            reports.append(file)

    return reports

def getPricingAverage(brands):
    average_list = []
    for brand in brands:
        brand = brand["key"]


        precios = DatabaseManager("encuentra24").count_price(brand)
        ds = []
        for item in precios:
            item = item[0]


            locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' ) 
            try:
                n = locale.atoi(item.split("B/.")[1])
                ds.append(n)
            except IndexError:
                # print("{} FAILED".format(item))
                pass



        inp_lst = ds
        list_avg = mean(inp_lst) 

        numbers = "{:,}".format(int(str(round(list_avg,3)).split(".")[0]))
     
        average_list.append({
            "brand": brand,
            "average": int(numbers.replace(',', '')),
            "average_locale": "B/.{}".format(numbers)
        })

    return average_list
    



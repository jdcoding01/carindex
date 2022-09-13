import requests
import time
from datetime import datetime as dt
from datetime import date

def getSessionData():
    count = requests.get("http://localhost:5000/scan/session")

    return count.text


def startSession():
    while True:
        data = getSessionData()
        time.sleep(4)


        current = str(dt.now()).split(" ")[1].split(".")[0].split(":")[1]

        if (int(current) - int(data.split('/')[1].split(':')[1]) >= 1):
            print("Stopped.")
            # with open('./scans/scan-{}.txt'.format(date.today()), "w") as scan:
            #     scan.write("done")
            #     scan.close()
            break
        else:
            print(data)

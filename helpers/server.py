from urllib import request
from flask import Flask
from flask import request, send_file
import analytics
import os

app = Flask(__name__)

@app.route('/',  methods = ['GET', 'POST', 'DELETE'])
def index():
    topBrands = analytics.getMostPopular()
    reports = analytics.getReports()
    average = analytics.getPricingAverage(topBrands)

    if request.method == "GET":
        return {
            "topBrands": topBrands,
            "reports": reports,
            "average": average
        }
   
    if request.method == "POST":
        content = request.json
        print(content['eventType'])
        return content

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
#!/usr/bin/python3

import requests

def main():
    mylookup = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&outputsize=full&apikey=CU4IW91M0YFZXVJI"
    stockdata = requests.get(mylookup)
    #print (stockdata.content)
    print (stockdata.json())
    decodedstockdata = stockdata.json()
    print (decodedstockdata["Time Series (5min)"]["019-08-20 10:20:00"])

main()

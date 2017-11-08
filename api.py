#!/Users/bin/python3

import requests


def convert():
    

    # takes user input for amount ot convert
    toConvert = self.inputField.get()

    # fetches current price for USD
    response = requests.get(url="https://goo.gl/PbAhsZ")

    # converts the response
    jsonResponse = response.json()

    # fetches list of currency
    priceList = jsonResponse["quotes"]

    # fetches USD to INR Conversion rate
    usdinr = priceList["USDINR"]

    # Output
    print(float(toConvert) * usdinr)

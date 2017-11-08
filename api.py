#!/Users/bin/python3

import requests


def convert():
    print("Enter the amount to Convert from USD to INR : ")

    # takes user input for amount ot convert
    toConvert = input()

    # fetches current price for USD
    response = requests.get(url="https://goo.gl/PbAhsZ")

    # converts the response
    jsonResponse = response.json()

    # fetches list of currency
    priceList = jsonResponse["quotes"]

    # fetches USD to INR Conversion rate
    usdinr = priceList["USDINR"]

    # Output
    print("The current USD Price is : Rs." + str(usdinr))

    print(float(toConvert) * usdinr)

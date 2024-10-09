# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход валюту (USD, GBP, EUR) и возвращает цену биткойна в указанной валюте.
URL для запроса: https://api.coindesk.com/v1/bpi/currentprice.json
'''


import requests


def get_bitcoin_price(currency):
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    data = response.json()

    if currency in data['bpi']:
        return data['bpi'][currency]['rate']


print(get_bitcoin_price("USD"))
print(get_bitcoin_price("GBP"))
print(get_bitcoin_price("EUR"))

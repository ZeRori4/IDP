# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает в качестве аргумента URL, делает к переданному URL GET запрос и возвращает,
успешен запрос или нет.
'''


import requests


url_test_ok = 'https://httpbin.org/get'
url_test_fail = 'https://httpbin.org/get1'


def status_requests(url):
    response = requests.get(url)
    if response.status_code == 200:
        return "Запрос успешен"
    return "Запрос не успешен"


print(status_requests(url_test_ok))
print(status_requests(url_test_fail))

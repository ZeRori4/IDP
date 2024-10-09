# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает в качестве аргумента URL, делает к переданному URL GET запрос и возвращает код
ответа. Если ответ говорит, что запрос неуспешен, нужно вывести соответствующую ошибку.
'''


import requests


url_test_ok = 'https://httpbin.org/get'
url_test_fail = 'https://httpbin.org/get1'


def status_requests(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.status_code
    return response.raise_for_status()#"The request was unsuccessful. status_code: {}".format(response.status_code)


print(status_requests(url_test_ok))
print(status_requests(url_test_fail))

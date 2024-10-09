# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает в качестве аргумента URL, делает к переданному URL GET запрос и возвращает список
всех атрибутов и методов, которые есть у результата запроса.
'''


import requests


test_url = 'https://httpbin.org/get'


def dir_requests(url):
    response = requests.get(url)
    return dir(response)


print(dir_requests(test_url))

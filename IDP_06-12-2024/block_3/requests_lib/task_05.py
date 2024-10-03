# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает id поста и возвращает этот пост в формате словаря.
URL для запроса: https://jsonplaceholder.typicode.com/posts
'''


import requests


url_test_ok = "https://jsonplaceholder.typicode.com/posts"


def get_id_requests(url):
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        return [{'id': item['id']} for item in posts]


print(get_id_requests(url_test_ok))

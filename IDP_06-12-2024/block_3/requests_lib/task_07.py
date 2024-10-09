# -*- coding: utf-8 -*-

"""
Напишите функцию, которая делает POST запрос и возвращает статус и созданный объект. Запрос содержит все необходимые
поля (придумать самому). URL для запроса: https://jsonplaceholder.typicode.com/posts
"""


import requests


def create_post(title, body, user_id):
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    response = requests.post(url, json=payload)
    return response.status_code, response.json()


status, created_object = create_post("asd", "qweqwe123", 1)
print("status:", status)
print("new obj:", created_object)

# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход строку в формате json и возвращает десериализованный python-объект.
Если объект не удается десериализовать, выбрасывайте ошибку: ‘Не удалось десериализовать: <входная строка>’
'''


import json

def deserialize_json(json_str):
    try:
        return json.loads(json_str)
    except ValueError:
        raise ValueError("Не удалось десериализовать: {}".format(json_str))


json_string = '{"name": "Anton", "age": 31}'
print(deserialize_json(json_string))

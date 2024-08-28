# -*- coding: utf-8 -*-

'''
Создайте функцию, которая принимает путь до файла и возвращает количество строк в файле. Если по указанному пути
директория, выбрасывайте ошибку 'Указанный путь <path> - директория'.
'''


import json

def deserialize_json(json_str):
    try:
        return json.loads(json_str)
    except ValueError:
        raise ValueError("Не удалось десериализовать: {}".format(json_str))


json_string = '{"name": "Anton", "age": 31}'
print(deserialize_json(json_string))

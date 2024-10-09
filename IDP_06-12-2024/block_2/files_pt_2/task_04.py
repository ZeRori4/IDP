# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход файловый поток к json файлу и возвращает python-объект.
Если объект не удается десериализовать, выбрасывайте ошибку: ‘Не удалось десериализовать: <object>’.
'''


import json


def load_json(file_stream):
    try:
        return json.load(file_stream)
    except Exception:
        raise Exception('Не удалось десериализовать: {}'.format(e))


json_data = '{"name": "Anton", "age": 31}'
with open('data.json', 'w') as fp:
    json.dump(json_data, fp)

with open('data.json', 'r') as fp:
    print(json.load(fp))

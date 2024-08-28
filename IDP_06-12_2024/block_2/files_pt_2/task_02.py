# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход python-объект и число отступов при сериализации. Функция должна возвращать
строку в формате json с соответствующим числом отступов.
Если объект не удается сериализовать, выбрасывайте ошибку: ‘Не удалось сериализовать: <object>’.
'''


import json


def serialize_to_json(obj, indent):
    try:
        return json.dumps(obj, indent=indent)
    except Exception:
        raise Exception('Не удалось сериализовать: {}'.format(obj))


object_dict = {"name": "Anton", "age": 31}
print(serialize_to_json(object_dict, 2))

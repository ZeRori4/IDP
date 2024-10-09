# -*- coding: utf-8 -*-

'''
Напишите функцию, которая валидирует новые имена объектов в системе на предмет запрещенных символов (!@#^&*).
Функция принимает новое имя объекта и, если оно содержит запрещенный символ, выбрасывает ошибку InvalidObjectNameError
с указанием на проблемный символ.
'''


import re


class InvalidObjectNameError(Exception):
    pass


def validate_object_name(object_name):
    if re.search(r'[!@#^&*]', object_name):
        raise InvalidObjectNameError("Имя объекта '{}' содержит недопустимые символы.".format(object_name))


try:
    validate_object_name("asdqwe_@name")
    print("Имя объекта допустимо.")
except InvalidObjectNameError as e:
    print(e)

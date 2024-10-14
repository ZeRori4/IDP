# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход произвольное число объектов и проверяет, являются ли они вызываемыми.
Если являются, то осуществите вызов каждого. Если хотя бы один не является, то выбрасывайте ошибку для пользователя,
что данный тип не является вызываемым.
'''


def valid_list_obj(*args):
    valid_list = []
    try:
        for obj in args:
            if not callable(obj):
                raise TypeError
        for obj in args:
            valid_list.append(obj())
        print(valid_list)
    except TypeError:
        print("Объект - {} не вызываемый".format(obj))


def callable_func():
    return "call func"


valid_list_obj(lambda: "lambda func", callable_func)

valid_list_obj(lambda: "lambda func", callable_func())  # проверка ошибки

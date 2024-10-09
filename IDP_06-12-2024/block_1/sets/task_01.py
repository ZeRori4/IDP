# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход строку и возвращает множество её
символов.
'''


def get_set_list_str(string):
    return set(string)


string_1 = "qweqwewerert"

print(get_set_list_str(string_1))

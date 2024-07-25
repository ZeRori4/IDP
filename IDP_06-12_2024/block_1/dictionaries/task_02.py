# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход строку и возвращает словарь, где
ключом является индекс символа в строке, а значением - символ, сохраняя только
чётные индексы.
'''


def get_dict_enum_odd(string):
    dictionary = {}
    for idx, sub_str in enumerate(string, 1):
        if idx % 2 == 0:
            dictionary[idx] = sub_str
    return dictionary


string_1 = "qweasd"

print(get_dict_enum_odd(string_1))

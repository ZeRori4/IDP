# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход строку и возвращает словарь, где
ключом является индекс символа в строке, а значением - символ.
'''


def get_dict_enum(string):
    dictionary = {}
    for idx, sub_str in enumerate(string, 1):
        dictionary[idx] = sub_str
    return dictionary


string_1 = "qwe"

print(get_dict_enum(string_1))

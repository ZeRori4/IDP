# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход строку и возвращает строку, в
которой нет повторяющихся элементов. ‘Мама мыла раму’ -> ‘Ма ылру’
'''


def get_set_str(string):
    return "".join(set(string))


string_1 = "qweqwewerert"

print(get_set_str(string_1))


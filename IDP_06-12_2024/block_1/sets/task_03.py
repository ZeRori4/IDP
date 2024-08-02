# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход строку и возвращает строку, в
которой нет повторяющихся элементов. ‘Мама мыла раму’ -> ‘Ма ылру’
'''


def get_set_str(full_str):
    show = set()
    return ''.join([sub_str for sub_str in full_str if not (sub_str in show or show.add(sub_str))])


string_1 = "q we qwew erert"

print(get_set_str(string_1))


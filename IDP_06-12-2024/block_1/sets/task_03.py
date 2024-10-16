# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход строку и возвращает строку, в
которой нет повторяющихся элементов. ‘Мама мыла раму’ -> ‘Ма ылру’
'''


def get_set_str(full_str):
    show = set()
    result = []
    for sub_str in full_str:
        lower_sub_str = sub_str.lower()
        if lower_sub_str not in show:
            show.add(lower_sub_str)
            result.append(sub_str)
    return ''.join(result)


string_1 = "Мама мыла раму"

print(get_set_str(string_1))

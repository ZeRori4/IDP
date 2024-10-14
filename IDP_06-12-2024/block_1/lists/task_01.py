# -*- coding: utf-8 -*-

'''
Реализуйте функцию, которая принимает на вход строку, преобразует ее в список
символов и возвращает его в отсортированном по убыванию виде.
'''


def sort_list(string):
    return sorted(string.split(), reverse=True)


string_1 = "a b c d c d f g"

print(sort_list(string_1))

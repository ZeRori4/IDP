# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход список списков и возвращает единый
список из всех элементов.
[[1, 2, 3], [4, 5, 6], [7], [8, 9]] -> [1, 2, 3, 4, 5, 6, 7, 8, 9].
'''


def flatten_list(original_list):
    result = []
    for element in original_list:
        if isinstance(element, list):
            result.extend(flatten_list(element))
        else:
            result.append(element)
    return result


list_1 = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]

print(flatten_list(list_1))

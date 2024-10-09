# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход список списков и возвращает один
объединенный список без повторяющихся элементов.
[[1, 2, 3], [2, 2, 4], [3, 1, 6]] -> [1, 2, 3, 4, 6].
'''


def set_list(lists):
    res_list = []
    for element in lists:
        res_list.extend(element)
    return set(res_list)


lists_1 = [[4, 4, 4], [1, 2, 3, 4], [3, 2, 1], [1, 1], [3, 3, 3]]

print(set_list(lists_1))

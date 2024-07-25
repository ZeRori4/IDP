# -*- coding: utf-8 -*-

'''
Напишите функцию, которая возвращает список [[1, 2, 3], [1, 2, 3], [1, 2, 3]].
'''


def get_list_of_lists(n):
    for i in range(1, n):
        list_numb = []
        list_numb.append(range(1, n+1))
    return list_numb * n


x1 = 4

print(get_list_of_lists(x1))

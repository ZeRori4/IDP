# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход целое положительное число n и
возвращает список из списков вида [[1, 2], [2, 3], [3, 4], ..., [n, n+1]].
'''


def get_list_of_lists(n):
    list_of_lists = []
    for i in range(1, n +1):
        list_numb = []
        list_numb.append(i)
        list_numb.append(i+1)
        list_of_lists.append(list_numb)
    return list_of_lists


x1 = 5

print(get_list_of_lists(x1))

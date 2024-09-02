# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход два множества и возвращает
множество, состоящее из элементов, которые есть во втором, но нет в первом
множестве. {1, 2, 3}, {3, 7, 1, 15} -> {7, 15}
'''


def get_set_symmetric_difference(x, y):
    return x.symmetric_difference(y)


x1 = {1, 2, 3, 4, 5}
y1 = {3, 4, 5, 6, 7}

print(get_set_symmetric_difference(x1, y1))

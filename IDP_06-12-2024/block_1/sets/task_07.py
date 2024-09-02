# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход два множества и возвращает булевский
флаг, означающий, является ли первое множество подмножеством второго.
'''


def get_bool_subset(x, y):
    return x.issubset(y)


x1 = {3, 4, 5}
y1 = {3, 4, 5, 6, 7}

print(get_bool_subset(x1, y1))

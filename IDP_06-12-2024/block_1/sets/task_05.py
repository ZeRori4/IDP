# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход два множества и возвращает
множество, состоящее из элементов, которые есть и в первом, и во втором
множествах. {1, 2, 3}, {3, 7, 1, 15} -> {1, 3}
'''


def get_set_intersection(x, y):
    return x.intersection(y)


x1 = {1, 2, 3, 4, 5}
y1 = {3, 4, 5, 6, 7}

print(get_set_intersection(x1, y1))
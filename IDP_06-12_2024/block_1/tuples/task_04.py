# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход натуральное число n, генерирует два
набора случайных действительных чисел от 0 до 1 длиной n и возвращает
объединённый кортеж из этих двух наборов.
'''

import random


def tuple_real_numbers(n):
    lst = ["{:0.", str(n), "f}"]
    full_str = "".join(lst)
    return (full_str.format(random.random()), full_str.format(random.random()))


n1 = 7
print(tuple_real_numbers(n1))

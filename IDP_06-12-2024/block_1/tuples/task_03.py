# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход целые числа x и n, генерирует n
случайных целых чисел от 1 до x включительно и возвращает кортеж из этих
случайных чисел без повторов.
'''


import random

def gen_random_set_numb_tuple(x, n):
    numb_list = []
    for i in range(n):
        random.randrange(1, x + 1)
        numb_list.append(random.randrange(1, x + 1))
    return tuple(set(numb_list))


x1 = 16
n1 = 16

print(gen_random_set_numb_tuple(x1, n1))


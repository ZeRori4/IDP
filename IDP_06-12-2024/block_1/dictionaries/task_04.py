# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход натуральные числа x и n, генерирует
n случайных целых чисел от 0 до x включительно и возвращает словарь,
где ключ — это число, а значение — это количество вхождений этого числа в
случайную последовательность.
'''

import random

def gen_random_dict(x, n):
    rand_numb_list = [random.randint(0, x) for _ in range(n)]
    print(rand_numb_list)
    numbers_match = {}
    for num in rand_numb_list:
        if num in numbers_match:
            numbers_match[num] += 1
        else:
            numbers_match[num] = 1
    return numbers_match

x1 = 1
n1 = 5
print(gen_random_dict(x1, n1))

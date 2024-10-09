# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход натуральное число n и возвращает
словарь вида {(1, 2): 1+2, (2, 3): 2+3, (3, 4): 3+4, ..., (n, n+1): n + n + 1}
с кортежами в качестве ключей.
'''


def get_dict_sum_idx1_and_idx2_range(n):
    dict_range = {}
    for idx in range(1, n + 1):
        dict_range[(idx, idx + 1)] = idx + (idx+1)
    return dict_range


n1 = 5

print(get_dict_sum_idx1_and_idx2_range(n1))

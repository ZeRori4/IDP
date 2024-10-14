# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход целочисленный кортеж и возвращает
этот кортеж без чётных чисел.
'''


def get_odd_numb(tpl):
    odd_numbs = []
    for idx in tpl:
        if idx % 2 == 1:
            odd_numbs.append(idx)
    return tuple(odd_numbs)


tuple_1 = (1, 2, 3, 4, 5, 6, 7, 8)

print(get_odd_numb(tuple_1))

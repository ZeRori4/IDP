# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход список и возвращает этот же список,
циклически сдвинутый вправо на один элемент (1, 2, 3, 4, 5 -> 5, 1, 2, 3, 4).
Задачу нужно решать с помощью срезов.
'''


def get_shift_numbers_list(list_numb):
    without_last_numb = list_numb[1:-1]
    last_numb = list_numb[-1:]
    return last_numb + without_last_numb


list_numb_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(get_shift_numbers_list(list_numb_1))

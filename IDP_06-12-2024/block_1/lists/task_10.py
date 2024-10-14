# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход целые числа x и y и возвращает
список последовательных нечётных целых чисел от x до y включительно без чисел,
делящихся на 3. Если x > y, то поменяйте их порядок.
'''


def get_odd_numbers_and_on_dir_3(x, y):
    # odd_numbers_list = []
    # for num in range(min(x, y), max(x, y) + 1):
    #     if num % 2 != 0:
    #         if num % 3 != 0:
    #             odd_numbers_list.append(num)
    # return odd_numbers_list
    return [num for num in range(min(x, y), max(x, y) + 1) if num % 2 != 0 if num % 3 != 0]

x1 = 5
y1 = 15

print(get_odd_numbers_and_on_dir_3(x1, y1))

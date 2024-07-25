# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход целые числа x и y и возвращает
список последовательных нечётных целых чисел от x до y включительно. Если x > y,
то поменяйте их порядок.
'''


def get_odd_numbers(x, y):
    odd_numbers_list = []
    if x < y:
        for num in range(x, y + 1):
            if num % 2 != 0:
                odd_numbers_list.append(num)
    else:
        for num in range(y, x + 1):
            if num % 2 != 0:
                odd_numbers_list.append(num)
    return odd_numbers_list


x1 = 5
y1 = 15

print(get_odd_numbers(x1, y1))

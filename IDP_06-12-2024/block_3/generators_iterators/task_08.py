# -*- coding: utf-8 -*-

"""
Реализуйте функцию-генератор, которая принимает список чисел и функцию и последовательно возвращает результаты
вычисления функции для каждого из чисел.
"""


def generator_function(numbers, func):
    for number in numbers:
        yield func(number)


numbers = [1, 2, 3, 4, 5]

def square(x):
    return x * x

gen = generator_function(numbers, square)

for result in gen:
    print(result)

# -*- coding: utf-8 -*-

'''
Напишите рекурсивную функцию, которая возвращает факториал числа n.
'''


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(3))

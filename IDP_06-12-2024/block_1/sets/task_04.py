# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход натуральное число n и возвращает
множество, состоящее только из чётных чисел от 0 до n.
'''


def get_set_odd_numbers(n):
    odd_numbers = []
    for i in range(0, n):
        if i % 2 == 0:
            odd_numbers.append(i)
    return set(odd_numbers)


x1 = 6
print(get_set_odd_numbers(x1))

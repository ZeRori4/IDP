# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход целые числа x и y и возвращает
список последовательных целых чисел от x до y включительно. Используйте list
comprehension. Если x > y, то поменяйте их порядок.
'''


def get_range(x, y):
    if x < y:
        return [i for i in range(x, y+1)]
    else:
        return [i for i in range(y, x+1)]


x1 = 5
y1 = 10

print(get_range(x1, y1))

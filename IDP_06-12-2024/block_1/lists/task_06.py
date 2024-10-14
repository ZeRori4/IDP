# -*- coding: utf-8 -*-

'''
Аналогично задаче 5, но с использованием встроенной функции map.
'''


def get_range(x, y):
    if x < y:
        return list(map(lambda i: i**2, range(x, y+1)))
    else:
        return list(map(lambda i: i**2, range(y, x+1)))


x1 = 5
y1 = 10

print(get_range(x1, y1))

# -*- coding: utf-8 -*-

'''
Реализуйте функцию, которая первым аргументом принимает число N, вторым
аргументом - список. Первый аргумент обязательный, второй - необязательный
(если не передан, считаем, что список пустой). Внутри функции добавьте в список
числа от 0 до N.
'''


def add_list_range(numb, list_optional=None):
    if list_optional is None:
        list_optional = []
    for i in range(0, numb + 1):
        list_optional.append(i)
    return list_optional


numb_1 = 5
lst = [2, 3]

print(add_list_range(numb_1, lst))

# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход целые числа a, b, c, d, генерирует
два последовательных целочисленных списка от a до b и от c до d включительно и
возвращает объединенный список. Если a > b или c > d, то поменяйте их порядок.
Объединение списков нужно осуществить разными способами (не менее трех).
'''


def get_list_ab_cd(a, b, c, d):
    list_ab = []
    list_cd = []
    if a < b:
        for num in range(a, b + 1):
            list_ab.append(num)
    else:
        for num in range(b, a + 1):
            list_ab.append(num)
    if c < d:
        for num in range(c, d + 1):
            list_cd.append(num)
    else:
        for num in range(d, c + 1):
            list_cd.append(num)
    return list_ab + list_cd


a1 = 9
b1 = 6
c1 = 20
d1 = 10

print(get_list_ab_cd(a1, b1, c1, d1))

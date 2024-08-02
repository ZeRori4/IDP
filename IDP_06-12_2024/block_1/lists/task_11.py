# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход целые числа a, b, c, d, генерирует
два последовательных целочисленных списка от a до b и от c до d включительно и
возвращает объединенный список. Если a > b или c > d, то поменяйте их порядок.
Объединение списков нужно осуществить разными способами (не менее трех).
'''


def get_list_ab_cd(a, b, c, d):
    # list_ab = []
    # list_cd = []
    # start_ab = min(a, b)
    # end_ab = max(a, b)
    # for num in range(start_ab, end_ab + 1):
    #     list_ab.append(num)
    # start_cd = min(c, d)
    # end_cd = max(c, d)
    # for num in range(start_cd, end_cd + 1):
    #     list_cd.append(num)
    # return list_ab + list_cd
    return [num for num in range(min(a, b), max(a, b) + 1)] + [num for num in range(min(c, d), max(c, d) + 1)]


a1 = 9
b1 = 6
c1 = 20
d1 = 15

print(get_list_ab_cd(a1, b1, c1, d1))

# -*- coding: utf-8 -*-

'''
Реализуйте функцию, которая принимает на вход список списков. В каждом из
вложенных списков может быть не менее двух элементов. Возвращаемый список должен
быть отсортирован по возрастанию второго элемента подсписка.
'''


def sort_element(lists):
    return sorted(lists, key=lambda x: x[1])


lists_1 = [[4, 4, 4], [1, 2, 3, 4], [3, 2, 1], [1, 1], [3, 3, 3]]

print(sort_element(lists_1))

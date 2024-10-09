# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает итерируемый объект. Она должна эмулировать работу цикла for с помощью цикла while и
метода next. Ошибка StopIteration должна быть обработана.
'''


def emulate_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            element = iterator.next()
            print(element)
        except StopIteration:
            break


list_1 = [1, 2, 3, 4, 5]
emulate_for(list_1)

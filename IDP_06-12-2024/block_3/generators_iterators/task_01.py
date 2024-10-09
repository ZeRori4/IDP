# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает итерируемый объект и возвращает объект итератор. Если на вход передается не
итерируемый объект, выбрасывайте ошибку (NonIterationObjectError).
'''


class NonIterationObjectError(Exception):
    pass


def to_iterator(obj):
    if not hasattr(obj, '__iter__'):
        raise NonIterationObjectError("Provided object is not iterable.")
    return iter(obj)


list_1 = [1, 2, 3, 4]
int_1 = 1

print(to_iterator(int_1))

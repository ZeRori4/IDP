# -*- coding: utf-8 -*-

'''
Напишите рекурсивную функцию, которая раскрывает все вложенные списки.
[[1, 2], 3, 4, [5, [6, 7], [8, 9, 10]], [[11, 12, [13]], [14, 15]] -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

'''


def flatten_list(original_list):
    result = []
    for element in original_list:
        if isinstance(element, list):
            result.extend(flatten_list(element))
        else:
            result.append(element)
    return result


orig_list_1 = [[1, 2], 3, 4, [5, [6, 7], [8, 9, 10]], [[11, 12, [13]], [14, 15]]]

print(flatten_list(orig_list_1))

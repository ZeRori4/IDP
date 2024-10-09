# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход список строк и возвращает количество
дублирующих строк списка. [‘a’, ‘b’, ‘c’, ‘a’, ‘a’, ‘b’, ‘b’] -> 4
'''


def get_count_duplicates(list_str):
    return len(list_str) - len(set(list_str))


list_str1 = ["a", "b", "c", "a", "a", "b", "b"]

print(get_count_duplicates(list_str1))

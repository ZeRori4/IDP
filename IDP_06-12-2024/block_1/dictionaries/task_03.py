# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход строку, преобразует ее в словарь,
где ключом является индекс символа в строке, а значением - символ, и возвращает
    ◦ список ключей словаря,
    ◦ список значений словаря,
    ◦ список пар (кортежей) ключ-значение, отсортированный по возрастанию
    значения.
'''


def get_lists_dicts(string):
    dictionary = {}
    for idx, sub_str in enumerate(string, 1):
        dictionary[idx] = sub_str
    return (
        list(dictionary.keys()),
        list(dictionary.values()),
        list(sorted(dictionary.items()))
    )


string_1 = "qwe"

print(get_lists_dicts(string_1))

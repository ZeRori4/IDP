# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход строку и возвращает список символов,
индексы которых кратны пяти.
'''


def get_list_idx_to_5(string):
    result = []
    for idx in range(len(string)):
        if idx % 5 == 0:
            result.append(string[idx])
    return result


string_1 = "asd dsa  zxc   wer asd  ert asdqwe sdf   sdf  "

print(get_list_idx_to_5(string_1))


# -*- coding: utf-8 -*-

'''
Реализуйте функцию, которая принимает на вход строку и символ и возвращает
строку без указанного символа (нужно удалить все вхождения).
'''


def del_substring(string, substring):
    return string.replace(substring, "")


string_1 = "asd dsa  zxc   wer asd  ert asdqwe sdf   sdf  "

print(del_substring(string_1, "asd"))

# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает строку и возвращает, содержит ли строка только латинские символы (верхний и нижний
регистр), цифры и пробелы.
'''


def is_valid_string(s):
    for sub_s in s:
        if not (sub_s.isalpha() or sub_s.isdigit() or sub_s.isspace()):
            return False
    return True


print(is_valid_string("ASD qwe 123"))

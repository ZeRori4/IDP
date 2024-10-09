# -*- coding: utf-8 -*-

'''
Напишите функцию, которая в качестве аргументов принимает строку и символ, а
возвращает:
   ◦ число вхождений этого символа в строку,
   ◦ строку, в которой указанный символ заменен пробелом.
'''


def count_end_replace_string(string, substring):
    return string.count(substring), string.replace(substring, " ")


string_1 = "asd dsa  zxc   wer asd  ert asdqwe sdf   sdf  "

print(count_end_replace_string(string_1, "asd"))


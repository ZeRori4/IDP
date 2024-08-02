# -*- coding: utf-8 -*-

'''
Реализуйте функцию, которая принимает на вход список символов, а возвращает
строку из этих символов, разделенных символом подчеркивания.
'''


def reverse_word_string(full_str):
    result = [
        letter.upper() if letter.islower() else
        letter.lower() if letter.isupper() else
        " " if letter.isspace() else ""
        for letter in full_str
    ]
    return "".join(result)


string_1 = "asd DDsa  zxc  123 wer   32eWERFDSt FSDFsdfSFe sdf   sdf  "

print(reverse_word_string(string_1))

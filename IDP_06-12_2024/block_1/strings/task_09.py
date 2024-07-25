# -*- coding: utf-8 -*-

'''
Реализуйте функцию, которая принимает на вход список символов, а возвращает
строку из этих символов, разделенных символом подчеркивания.
'''


def reverse_word_string(string):
    result = []
    for letter in string:
        if letter.isdigit():
            letter = ""
            result.append(letter)
        elif letter.islower():
            letter = letter.upper()
            result.append(letter)
        elif letter.isupper():
            letter = letter.lower()
            result.append(letter)
        elif letter.isspace():
            letter = " "
            result.append(letter)
    return "".join(result)


string_1 = "asd DDsa  zxc  123 wer   32eWERFDSt FSDFsdfSFe sdf   sdf  "

print(reverse_word_string(string_1))

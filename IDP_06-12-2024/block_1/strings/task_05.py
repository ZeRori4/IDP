# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход строку и возвращает новую строку, в
которой каждый из символов, кроме пробела, удвоен.
'''

def duble_letter_string(string):
    result = []
    for letter in string:
        if letter.isalnum():
            letter = letter + letter
            result.append(letter)
        else:
            if letter.isspace():
                result.append(letter)
    return "".join(result)

string_1 = "asd dsa  zxc   wer asd  ert asdqwe sdf   sdf  "

print(duble_letter_string(string_1))

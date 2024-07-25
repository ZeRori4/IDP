# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход строку и возвращает список индексов
всех слов строки (по первой букве).
'''

def idx_word_string(string):
    result = []
    word = ''
    for idx, letter in enumerate(string):
        if letter.isspace():
            if word:
                result.append(idx - len(word))
                word = ''
        else:
            word += letter
    return result


string_1 = "ads dsa  zxc   wer asd  ert asdqwe sdf   sdf  "

print(idx_word_string(string_1))

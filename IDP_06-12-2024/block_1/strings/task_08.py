# -*- coding: utf-8 -*-

'''
Реализуйте функцию, которая принимает на вход список символов, а возвращает
строку из этих символов, разделенных символом подчеркивания.
'''

def reverse_word_string(string):
    result = []
    word = ''
    for letter in string:
        if letter.isspace():
            if word:
                result.append(word)
                word = ''
        else:
            word += letter
    return " ".join(result[::-1])


string_1 = "asd dsa  zxc   wer   ert qwe sdf   sdf  "

print(reverse_word_string(string_1))

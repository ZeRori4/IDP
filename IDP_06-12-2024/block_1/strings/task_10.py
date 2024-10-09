# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход строку, ищет в этой строке слова
палиндромы и возвращает первый найденный палиндром.
'''


def is_palindrome(string):
    result = []
    word = ''
    for letter in string:
        if letter.isspace():
            #print("нашёл пробел %s" % letter)
            if word:
                s_lower = word.lower()
                if s_lower == s_lower[::-1]:
                    #print("вывод первого слово палиндрома: %s" % s_lower)
                    return s_lower
                result.append(word)
                word = ''
                #print("добавил слово %s" % result)
        else:
            word += letter
            #print("собираю буквы %s" % word)
    return


string_1 = "assra dsa  zxc   wer  fgfgfgf ert qwq sdf   sdf  "

print(is_palindrome(string_1))

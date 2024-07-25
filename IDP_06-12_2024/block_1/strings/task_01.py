# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход строку и возвращает список слов.
Слова разделены одним и/или более пробелами. Разделите полученную строку на
слова, не используя строковые методы. В следующих задачах (2–10) для обработки
случая, в котором на вход поступает строка с более чем одним пробелом между
словами/символами, можете переиспользовать функцию, полученную в задаче 1.
'''


# def split_string_1(string):
#     return string.split()  # строковый метод ;(


def split_string_2(string):
    result = []
    word = ''
    for letter in string:
        if letter.isspace():  # строковый метод ;(
            print("нашёл пробел %s" % letter)
            if word:
                result.append(word)
                word = ''
                print("добавил слово %s" % result)
        else:
            word += letter
            print("собираю буквы %s" % word)
    return result


string_1 = "asd dsa  zxc   wer   ert qwe sdf   sdf  "

#print(split_string_1(string_1))
print(split_string_2(string_1))

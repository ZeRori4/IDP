# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает строку и возвращает словарь, ключами которого являются хештеги из текста, а
значениями - количество вхождений данного тега. Под хештегом будем понимать #XxxxXxxx, т. е. любое слово, сразу после
символа # без пробелов. Ключами выходного словаря должны быть слова без символа #.

'''


import re


def count_hashtags(text):
    hashtags = re.findall(r'#(\w+)', text)
    hashtag_count = {}
    for tag in hashtags:
        if tag in hashtag_count:
            hashtag_count[tag] += 1
        else:
            hashtag_count[tag] = 1
    return hashtag_count


text = "Это пример текста с #хештегом и еще одним #хештегом. #хештегом"
print(count_hashtags(text))

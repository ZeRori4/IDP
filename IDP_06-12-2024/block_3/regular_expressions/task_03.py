# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает строку и возвращает, является ли строка номером мобильного телефона (+7 или 8).
'''

import random

import re


def is_mobile_number(phone_number):
    pattern = r'^(?:\+7|8)\d{10}$'
    if re.match(pattern, phone_number):
        return True
    else:
        return False


print(is_mobile_number("+71234567890"))

# -*- coding: utf-8 -*-

"""
Напишите функцию, которая принимает на вход строку и возвращает первое вхождение подстроки, которая может являться
trassir guid.
"""

import re


def find_trassir_guid(input_string):
    pattern = r'\b[A-Za-z]{8}\b'
    match = re.search(pattern, input_string)
    if match:
        return match.group(0)
    else:
        return None


input_string = "Это пример строки с guid: Abcdefgh и другими символами."
print(find_trassir_guid(input_string))

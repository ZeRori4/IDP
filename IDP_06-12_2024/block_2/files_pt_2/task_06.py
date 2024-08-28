# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход строку в base64 формате и возвращает декодированную в utf-8
'''


import base64


def decode_base64_to_str(base64_string):
    data = base64.b64decode(base64_string)
    return data.decode('utf-8')

print(decode_base64_to_str("0J/RgNC40LLQtdGCINC/0L7RgdC10YLQuNGC0LXQu9GMIQ=="))
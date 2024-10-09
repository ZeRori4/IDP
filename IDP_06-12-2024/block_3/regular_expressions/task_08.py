# -*- coding: utf-8 -*-

"""
Напишите функцию, которая принимает строку и возвращает, является ли эта строка URL адресом:
  ◦ протокол http или https,
  ◦ IP-адрес (v4) или localhost,
  ◦ опционально может быть указан порт.
"""


import re


def is_valid_url(url):
    pattern = re.compile(
        r'^(http://|https://|localhost|(\d{1,3}\.){3}\d{1,3})(:\d+)?(/.*)?$'
    )
    return bool(pattern.match(url))


print(is_valid_url("https://translate.google.com/?hl=ru&sl=auto&tl=ru&op=translate"))
print(is_valid_url("192.168.1.1:5000"))
print(is_valid_url("localhost"))

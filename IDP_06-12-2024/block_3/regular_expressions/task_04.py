# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает строку и проверяет, является ли строка денежной суммой в долларах
(формат - $1000.00). Если не является, то выбрасывает ошибку пользователю (InvalidFormatError).
'''

import re


class InvalidFormatError(Exception):
    pass


def check_dollar_amount(amount):
    pattern = r'^\$\d{1,3}(,\d{3})*(\.\d{2})?$'
    if not re.match(pattern, amount):
        raise InvalidFormatError("Invalid format: The amount must be in the format $1000.00")
    return True


try:
    print(check_dollar_amount("$1,000.00"))
    print(check_dollar_amount("$1000"))
except InvalidFormatError as e:
    print(e)

# -*- coding: utf-8 -*-

'''
Создайте функцию, которая принимает дату в строковом формате ("ГГГГ/ММ/ДД"), а затем проверяет, находится ли указанная
точка в будущем или прошлом относительно текущего момента.
Результат возвращается в формате 'Будущее', 'Прошлое', 'Настоящее'.
'''

import datetime


def check_date(date_str):
    current_date = datetime.date.today()
    input_date = datetime.datetime.strptime(date_str, "%Y/%m/%d").date()
    if input_date > current_date:
        return 'Будущее'
    elif input_date < current_date:
        return 'Прошлое'
    else:
        return 'Настоящее'


date_input = "2024/08/13"
print(check_date(date_input))

# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает дату рождения пользователя в формате строки "ГГГГ-ММ-ДД" и возвращает его возраст в
полных годах.
'''

from datetime import datetime


def get_age(birthday):
    today = datetime.today()
    date = datetime.strptime(birthday, "%Y-%m-%d")
    age = today.year - date.year
    if (today.month, today.day) < (date.month, date.day):
        age -= 1
    return age


birthday_anton = "1993-03-11"
print(get_age(birthday_anton))

# -*- coding: utf-8 -*-

'''
Реализуйте функцию, которая принимает две даты типа datetime и определяет, сколько времени прошло между ними. Верните
результат в разных форматах (в днях, часах и секундах).
'''


import datetime


def get_diff_date(x, y):
    diff = x - y
    days = diff.days
    seconds = diff.total_seconds()
    hours = seconds // 3600
    return days, int(hours), int(seconds)


input_date_1 = datetime.date(2024, 7, 19)
input_date_2 = datetime.date(2024, 7, 13)

print(get_diff_date(input_date_1, input_date_2))

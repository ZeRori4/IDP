# -*- coding: utf-8 -*-

'''
Реализуйте функцию, которая принимает две даты в строковом формате ("ГГГГ-ММ-ДД ЧЧ:ММ:СС") и определяет, сколько
времени прошло между ними. Верните результат в разных форматах (в днях, часах и секундах).
'''



from datetime import datetime


def get_diff_str_date(str_date1, str_date2):
    dt1 = datetime.strptime(str_date1, "%Y-%m-%d %H:%M:%S")
    dt2 = datetime.strptime(str_date2, "%Y-%m-%d %H:%M:%S")
    diff = dt2 - dt1
    seconds = diff.total_seconds()
    hours = seconds // 3600
    days = hours // 24
    return int(days), int(hours), int(seconds)


input_date_1 = "2024-08-10 21:00:00"
input_date_2 = "2024-08-14 23:30:00"

print(get_diff_str_date(input_date_1, input_date_2))

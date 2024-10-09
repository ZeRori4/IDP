# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает timestamp (в секундах) и возвращает дату и время в формате "ГГГГ-ММ-ДД ЧЧ:ММ:СС"
'''


import datetime


def ts_to_str(ts):
    dt = datetime.datetime.fromtimestamp(ts)
    return dt.strftime('%Y-%m-%d %H:%M:%S')


timestamp = 1723411433

print(ts_to_str(timestamp))

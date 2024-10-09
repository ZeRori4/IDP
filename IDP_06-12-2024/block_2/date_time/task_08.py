# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает timestamp и возвращает utc и local datetime.
'''


import datetime


def timestamp_to_utc_dt_and_local_dt(ts):
    return datetime.datetime.utcfromtimestamp(ts), datetime.datetime.fromtimestamp(ts)


timestamp = 1723658549
print(timestamp_to_utc_dt_and_local_dt(timestamp))

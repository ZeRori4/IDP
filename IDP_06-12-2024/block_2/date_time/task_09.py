# -*- coding: utf-8 -*-

'''
Реализуйте программу, которая принимает timestamp и возвращает информацию об этом дне. Нужно вернуть, какой это день в
неделе по счету (понедельник = 0), какой это день недели по имени, какая неделя в году по счёту.
Например: 1712668126 -> (1, Tue, 15)
'''

import datetime


def info_day_from_ts(ts):
    dt = datetime.datetime.fromtimestamp(ts)
    return dt.weekday(), dt.strftime('%a'), dt.isocalendar()[1]


timestamp = 1723658549
print(info_day_from_ts(timestamp))

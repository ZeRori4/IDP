# -*- coding: utf-8 -*-

'''
Реализуйте функцию, которая принимает дату и время в формате datetime и возвращает количество оставшихся секунд до
полуночи.
'''

from datetime import datetime, timedelta


def get_sec_to_midnight(dt):
    midnight = datetime.combine(dt.date() + timedelta(days=1), datetime.min.time())
    return int((midnight - dt).seconds)


now = datetime.now()
print(get_sec_to_midnight(now))

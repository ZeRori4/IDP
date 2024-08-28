# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход натуральное число n и возвращает
множество, состоящее только из чётных чисел от 0 до n.
'''

from datetime import datetime, timedelta


def get_sec_to_midnight(dt):
    midnight = datetime.combine(dt.date() + timedelta(days=1), datetime.min.time())
    return int((midnight - dt).seconds)


now = datetime.now()
print(get_sec_to_midnight(now))

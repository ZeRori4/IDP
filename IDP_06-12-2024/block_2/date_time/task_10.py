# -*- coding: utf-8 -*-

'''
Напишите функцию, которая на вход принимает datetime, а возвращает строку с описанием давности события.
Например:
Если передана дата, которая отличается от текущей менее чем на 1 минуту (назад) -> только что
Дата менее часа назад - 18мин назад
Дата менее дня назад - 2ч назад
Дата более дня назад - 19д назад
'''


from datetime import datetime, timedelta


def get_event_ago(ev_time):
    time_diff = datetime.now() - ev_time
    if time_diff < timedelta(minutes=1):
        return "только что"
    elif time_diff < timedelta(hours=1):
        return "{}мин назад".format(int(time_diff.total_seconds() / 60))
    elif time_diff < timedelta(days=1):
        return "{}ч назад".format(int(time_diff.total_seconds() / 3600))
    else:
        return "{}д назад".format(time_diff.days)


event_time = datetime(2024, 8, 14, hour=15, minute=0, second=0)
print(get_event_ago(event_time))

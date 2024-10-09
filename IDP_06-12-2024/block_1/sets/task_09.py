# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход два списка - список покупателей за
первый и второй год существования интернет-магазина - и возвращает:
        ◦ множество новых покупателей за второй год
        ◦ множество потерянных покупателей, которые пользовались магазином в
        первый год, но во второй ушли
'''


def get_miss_and_new_shoppers(x, y):
    return set(y).difference(set(x)), set(x).difference(set(y))


year_1 = ["Jon", "Milla", "Rob", "Millana", "Mark"]
year_2 = ["Bill", "Milla", "Rob", "Mark"]

print(get_miss_and_new_shoppers(year_1, year_2))

# -*- coding: utf-8 -*-

"""
Напишите функцию, которая принимает на вход словарь с информацией о владении
фруктами (Приложение 1) и возвращает словарь, где ключами являются фрукты, а
значениями - их суммарное количество среди всех хозяев. Обратите внимание, что
количество и наименование фруктов заранее неизвестно.
fruit_owners = {
    "Ваня": {"apple": 10, "pear": 3, "peach": 1,},
    "Дима": {"apple": 4, "pear": 0, "peach": 0,},
    "Катя": {"apple": 3, "pear": 7, "peach": 3,},
}
"""


def aggregate_fruit_ownership(fruit_ownership):
    total_fruits = {}

    for owner, fruits in fruit_ownership.items():
        for fruit, quantity in fruits.items():
            if fruit in total_fruits:
                total_fruits[fruit] += quantity
                print("1 %s" % total_fruits)
            else:
                total_fruits[fruit] = quantity
                print("2 %s" % total_fruits)

    return total_fruits


x1 = {
    "Bill": {"apple": 10, "pear": 3, "peach": 1,},
    "Rell": {"apple": 3, "pear": 7, "peach": 3,},
    "Den": {"apple": 4, "pear": 0, "peach": 0,},
}

print(aggregate_fruit_ownership(x1))

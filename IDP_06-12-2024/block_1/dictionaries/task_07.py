# -*- coding: utf-8 -*-

"""
 Напишите функцию, которая принимает на вход
    • словарь с информацией о владении фруктами (Приложение 1),
    • название фрукта,
    • количество этого фрукта,
    • имя хозяина
и добавляет хозяину столько фруктов. Если в качестве хозяина передан None, то
фрукт добавляется всем. Если хозяина с заданным именем нет, то добавляется
запись о новом хозяине. Если у хозяина нет фрукта с заданным названием, то
добавляется запись о новом фрукте.
fruit_owners = {
    "Ваня": {"apple": 10, "pear": 3, "peach": 1,},
    "Дима": {"apple": 4, "pear": 0, "peach": 0,},
    "Катя": {"apple": 3, "pear": 7, "peach": 3,},
}
"""


def add_fruit(fruit_owner, fruit_name, quantity, owner):
    if owner is None:
        for existing_owner in fruit_owner:
            if fruit_name in fruit_owner[existing_owner]:
                fruit_owner[existing_owner][fruit_name] += quantity
            else:
                fruit_owner[existing_owner][fruit_name] = quantity
    else:
        if owner not in fruit_owner:
            fruit_owner[owner] = {}

        if fruit_name in fruit_owner[owner]:
            fruit_owner[owner][fruit_name] += quantity
        else:
            fruit_owner[owner][fruit_name] = quantity


fruit_owner = {
    "Bill": {"apple": 10, "pear": 3, "peach": 1},
    "Rell": {"apple": 3, "pear": 7, "peach": 3},
    "Den": {"apple": 4, "pear": 0, "peach": 0},
}

add_fruit(fruit_owner, "banana", 5, "Bill")
print(fruit_owner)

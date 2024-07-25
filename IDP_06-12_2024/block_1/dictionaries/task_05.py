# -*- coding: utf-8 -*-

"""
Напишите функцию, которая принимает на вход словарь с информацией о владении
фруктами (Приложение 1) и возвращает список имён владельцев, отсортированный по
количеству яблок - от большего к меньшему.
fruit_owners = {
    "Ваня": {"apple": 10, "pear": 3, "peach": 1,},
    "Дима": {"apple": 4, "pear": 0, "peach": 0,},
    "Катя": {"apple": 3, "pear": 7, "peach": 3,},
}
"""


def sort_owners_by_apples(fruit_owners):
    owners_with_apples = [
        (owner, fruits.get("apple", 0)) 
        for owner, fruits 
        in fruit_owners.items()
    ]
    print(owners_with_apples)
    sorted_owners = sorted(owners_with_apples, key=lambda x: x[1], reverse=True)
    print(owners_with_apples)
    sorted_names = [owner for owner, _ in sorted_owners]
    print(owners_with_apples)
    return sorted_names


x1 = {
    "Bill": {"apple": 10, "pear": 3, "peach": 1,},
    "Rell": {"apple": 3, "pear": 7, "peach": 3,},
    "Den": {"apple": 4, "pear": 0, "peach": 0,},
}

print(sort_owners_by_apples(x1))

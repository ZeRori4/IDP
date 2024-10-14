# -*- coding: utf-8 -*-

"""
Создайте свой класс CustomList, который наследуется от класса list и переопределяет метод extend, чтобы он добавлял
элементы в обратном порядке.
"""


class CustomList(list):
    def extend(self, iterable):
        for item in reversed(iterable):
            list.append(self, item)


my_list = CustomList([1, 2, 3])

my_list.extend([4, 5, 6])
print("new list: {}".format(my_list))


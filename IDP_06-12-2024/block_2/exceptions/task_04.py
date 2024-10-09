# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход список. Используя обработку исключений, рассортируйте объекты на три списка:
список строк, список чисел и список остальных типов - и верните их. Для сортировки не используйте if elif else.
'''


def sort_objects(obj_list):
    strings_list = []
    numbers_list = []
    others_list = []
    for obj in obj_list:
        try:
            if isinstance(obj, (int, float)):
                numbers_list.append(obj)
            else:
                raise TypeError
        except TypeError:
            try:
                if isinstance(obj, str):
                    strings_list.append(obj)
                else:
                    raise TypeError
            except TypeError:
                others_list.append(obj)

    return strings_list, numbers_list, others_list


objects_list = [2, 3, "asd", "ZXC", 2.2, 3.3, [1, 3, 5], {1: "a"}]
strings_list, numbers_list, others_list = sort_objects(objects_list)
print(strings_list)
print(numbers_list)
print(others_list)

# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход список и возвращает список из квадратов исходного.
Если элемент исходного списка не является числом и его нельзя возвести в квадрат, выбрасывайте ошибку
'Нельзя возвести в квадрат объект типа <type>'.
'''


def square_list_numbers(lst):
    res_list = []
    for num in lst:
        try:
            res = int(num) ** 2
            res_list.append(res)
        except ValueError:
            print("Нельзя возвести в квадрат объект типа {}. Объект: {}".format(type(num),num))
    print(res_list)


list_numbers = [3, 4, "d", 6, 8]

square_list_numbers(list_numbers)

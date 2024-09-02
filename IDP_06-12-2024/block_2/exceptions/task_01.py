# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает число от пользователя и возвращает его квадрат.
Обработайте исключение, если введено не число.
'''


def square_number(num):
    try:
        if isinstance(num, int):  # TODO пробовал и так , и num = int(num) либо float(num)
            res = num ** 2
            print("{}".format(res))
    except ValueError:
        print("Введено не число!")  # TODO почему-то выходит ошибка, а не исключение


number = input("Введите число: ")

square_number(number)

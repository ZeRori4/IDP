# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает два числа, делит первое число на второе и возвращает результат.
Обработайте исключение, если второе число равно нулю.
'''


def divide_numbers(num1, num2):
    try:
        res = float(num1) / float(num2)
        print("Деление чисел {} на {} равено {}".format(num1, num2, res))
    except ZeroDivisionError:
        print("Ошибка: Денить на 0 нельзя!")


nummer1 = input("Введите первое число: ")
nummer2 = input("Введите второе число: ")

divide_numbers(nummer1, nummer2)

# -*- coding: utf-8 -*-

'''
Напишите функцию, осуществляющую отложенный вызов другой функции. Используйте рекурсивные вызовы. Первым аргументом
передается количество секунд, вторым - функция, которую нужно вызвать (callback).
'''


import time


def delay_call(sec, callback):
    if sec <= 0:
        callback()
    else:
        print("ждём")
        time.sleep(1)
        delay_call(sec - 1, callback)


def another_function():
    print("функция another_function отработала")


delay_call(2, another_function)

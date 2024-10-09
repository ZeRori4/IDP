# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход имя файла и проверяет, существует ли файл с заданным именем в рабочей
директории. Результат верните в булевом формате.
'''


import os.path


def check_isfile(filename):
    return os.path.isfile(filename)


filename_1 = "task_01.py"
print(check_isfile(filename_1))

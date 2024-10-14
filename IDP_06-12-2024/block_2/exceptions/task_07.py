# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает произвольное количество строк. Если среди них есть строка, в которой менее трех
символов (не считая литерала \n), то вызывается ошибка ValueError.
'''



def str_validator(*args):
    for sub_str in args:
        if len(sub_str.replace("\n", "")) < 3:
            raise ValueError("Есть строка короче 3 символов")
    print("ok")

str_validator("228","322","w\nw2")

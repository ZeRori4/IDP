# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход путь до файла и текст. Функция создает новый файл или перезаписывает
имеющийся. Записывает в него заданный текст. Используйте контекстный менеджер для обращения к файлу.
'''


def write_test(full_path, test):
    with open(full_path, 'w') as file_obj:
        file_obj.write(test)


file_path = "C:/GitHub/IDP/IDP_06-12_2024/block_2/files_pt_2/task_01_exp.py"
write_test(file_path, "test")

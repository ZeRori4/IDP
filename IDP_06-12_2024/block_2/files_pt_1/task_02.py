# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход путь до файла и текст. Функция создает новый файл и записывает в него текст.
Если файл существует, то его содержимое перезаписывается.
'''


def write_test(full_path, test):
    with open(full_path, 'w') as file_obj:
        file_obj.write(test)


file_path = "C:/GitHub/IDP/IDP_06-12_2024/block_2/files_pt_1/task_02_exp.py"
write_test(file_path, "test test \n1\n1\n1\n1\n1\n1")

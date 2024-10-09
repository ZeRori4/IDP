# -*- coding: utf-8 -*-

'''
Создайте функцию, которая принимает на вход путь до файла. Если по указанному пути директория, покажите пользователю
ошибку 'Указанный путь <path> - директория'. Если по указанному пути файл, то удалите его.
'''


import os.path


def remove_file(full_path):
    if os.path.isdir(full_path):
        raise ValueError("Указанный путь '{}' - директория".format(full_path))
    os.remove(full_path)


file_path = "C:/GitHub/IDP/IDP_06-12_2024/block_2/files_pt_1/task_02_exp.py"
remove_file(file_path)

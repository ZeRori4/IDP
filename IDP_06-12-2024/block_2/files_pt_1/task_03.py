# -*- coding: utf-8 -*-

'''
Создайте функцию, которая принимает путь до файла и возвращает количество строк в файле. Если по указанному пути
директория, выбрасывайте ошибку 'Указанный путь <path> - директория'.
'''


import os


def count_lines_in_file(full_path):
    if os.path.isdir(full_path):
        raise ValueError("Указанный путь '{}' - директория".format(full_path))
    with open(full_path) as file_obj:
        return len(file_obj.readlines())


file_path = "C:/GitHub/IDP/IDP_06-12_2024/block_2/files_pt_1/task_02_exp.py"
print(count_lines_in_file(file_path))

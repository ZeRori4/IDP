# -*- coding: utf-8 -*-

'''
Реализуйте функцию, которая принимает на вход путь. Если по указанному пути файл, то открывает и возвращает содержимое.
Если это директория, то возвращает список файлов и поддиректорий этой директории.
'''


import os


def check_info_path(path):
    if os.path.isdir(path):
        return os.listdir(path)
    with open(path, 'r') as file_obj:
        return file_obj.read()


dir_path_1 = "C:/GitHub/IDP/IDP_06-12_2024/block_2/files_pt_1"
file_path = "C:/GitHub/IDP/IDP_06-12_2024/block_2/files_pt_1/task_02_exp.py"
print(check_info_path(file_path))

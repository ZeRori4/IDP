# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход путь. Если это путь до файла, удаляет указанный файл.
Если путь до директории, удаляет директорию рекурсивно.
'''


import os
import shutil


def delete_path(path):
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)


del_path = "C:/GitHub/IDP/IDP_06-12_2024/block_2/files_pt_1/test"

delete_path(del_path)

# -*- coding: utf-8 -*-

'''
Создайте функцию, которая принимает на вход путь до директории.
В указанной директории создается дочерняя директория test, внутри которой создается файл (имя файла <timestamp>.txt).
В него записывается полный путь до текущего файла.
'''


import os
import time


def write_in_new_file(dir_path):
    if os.path.isdir(dir_path):
        os.mkdir('test')
        timestamp = int(time.time())
        full_path = dir_path + '/test/' + '{}.txt'.format(timestamp)
        with open(full_path, 'w') as file_obj:
            file_obj.write(os.getcwd())


dir_path_1 = "C:/GitHub/IDP/IDP_06-12_2024/block_2/files_pt_1"
write_in_new_file(dir_path_1)

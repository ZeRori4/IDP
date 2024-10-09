# -*- coding: utf-8 -*-

'''
Реализуйте функцию, которая будет работать на windows. В качестве аргумента она должна принимать строку с расширением
файла, например, 'txt'. Функция должна подсчитать и вернуть суммарный размер в байтах файлов директории загрузок с
указанным расширением. Подсчет должен осуществляться на одном уровне без углубления в директории.
'''


import os


def get_total_size(extension):
    my_dir = "C:/GitHub/IDP/IDP_06-12_2024/block_2/files_pt_1"
    total_size = 0
    for filename in os.listdir(my_dir):
        if filename.endswith(extension):
            file_path = os.path.join(my_dir, filename)
            total_size += os.path.getsize(file_path)
    return total_size


print(get_total_size(".py"))

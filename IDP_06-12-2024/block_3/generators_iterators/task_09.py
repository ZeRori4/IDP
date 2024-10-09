# -*- coding: utf-8 -*-

"""
Реализуйте функцию-генератор, которая принимает путь до файла и возвращает его содержимое построчно. Если по указанному
пути файла не существует, выбрасывайте ошибку FileNotFoundError.
"""


import os


class FileNotFoundError(Exception):
    pass


def read_file_line_by_line(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError("Файл не найден: {}".format(file_path))

    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()


path = 'C:\\new_folder\\423.txt'
try:
    for line in read_file_line_by_line(path):
        print(line)
except FileNotFoundError as e:
    print(e)

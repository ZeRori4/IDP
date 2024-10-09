# -*- coding: utf-8 -*-

'''
Реализуйте функцию-генератор, которая принимает путь до директории, проходится по её python файлам и возвращает для
каждого количество строк, игнорируя пустые и комментарии. Обратите внимание, что комментарий может начинаться не с
первого символа строки.
'''

import os


def count_lines_in_python_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                line_count = 0
                with open(file_path, 'r') as f:
                    for line in f:
                        stripped_line = line.strip()
                        if stripped_line and not stripped_line.startswith('#'):
                            line_count += 1
                yield (file_path, line_count)


directory_path = 'C:\\new_folder\\'
for file_info in count_lines_in_python_files(directory_path):
    print("Файл: {}, Количество строк кода: {}".format(file_info[0], file_info[1]))

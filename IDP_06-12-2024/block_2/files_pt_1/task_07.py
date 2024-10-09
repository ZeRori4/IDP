# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход путь до файла и возвращает количество строк в файле. В родительской
директории входного файла создает 'log.txt', в который дописывает строку вида:
<текущее время ("ГГГГ-ММ-ДД ЧЧ:ММ:СС")>: <путь до входного файла> - <результат вычисления>.
'''


import os
from datetime import datetime


def loging_count_lines(full_path):
    with open(full_path) as file_obj:
        lines_file = len(file_obj.readlines())
    log_dir = os.path.dirname(full_path)
    full_path_log = os.path.join(log_dir, 'log.txt')
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = "{}: {} - {}\n".format(current_time, full_path, lines_file)
    with open(full_path_log, "a") as file_log:
        file_log.write(log_entry)


file_path_1 = "C:/GitHub/IDP/IDP_06-12_2024/block_2/files_pt_1/task_02_exp.py"
loging_count_lines(file_path_1)

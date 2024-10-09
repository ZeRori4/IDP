# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает путь до текстового файла и возвращает список вхождений в него дат в формате
"dd/mm/yyyy".
'''

import re


def extract_dates(file_path):
    date_pattern = r'\b(\d{2})\/(\d{2})\/(\d{4})\b'
    dates = []
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            dates = re.findall(date_pattern, content)
            dates = ['{}/{}/{}'.format(day, month, year) for day, month, year in dates]
    except IOError:
        print("Ошибка: Не удалось открыть файл.")
    return dates


file_path = 'C:/GitHub/IDP/IDP_06-12-2024/block_3/regular_expressions/file_123.txt'
print(extract_dates(file_path))

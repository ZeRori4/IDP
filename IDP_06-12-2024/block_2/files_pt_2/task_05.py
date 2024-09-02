# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход python-объект и имя файла с расширением .log.
Функция должна создать файл с указанным именем в рабочей директории, если его нет, и дописать в него новой строкой
переданные данные, преобразованные в json формат. Если объект не удается сериализовать, выбрасывайте ошибку:
‘Не удалось сериализовать: <object>’.
'''


import json
import os


def log_to_file(obj, filename):
    try:
        json_data = json.dumps(obj)
    except Exception:
        raise Exception("Не удалось сериализовать: %s" % obj)
    with open(os.path.join(os.getcwd(), filename), 'a') as fp:
        #json.dump(json_data + '\n', fp)
        fp.write(json_data + '\n')


data = {"name": "Anton", "age": 31}
log_to_file(data, 'data.log')

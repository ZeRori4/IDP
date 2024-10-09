# -*- coding: utf-8 -*-

'''
Реализуйте функцию, которая принимает две строки (имя файла и строка для записи).
Откройте файл и допишите с новой строки значение второго аргумента. Если аргументы не являются строками, выбрасывайте
AssertionError (assert). Обработайте исключения, связанные с открытием файла.
'''


def append_to_file(filename, text_str):
    assert isinstance(filename, str), "Имя файла должно быть строкой"
    assert isinstance(text_str, str), "Текст для записи должен быть строкой"
    try:
        with open(filename, 'a') as file:
            file.write(text_str + '\n')
    except AssertionError as e:
        print("Ошибка: {}".format(e))


append_to_file('file.txt', 'Текст строки')

# -*- coding: utf-8 -*-

'''
Используя библиотеки requests и BeautifulSoup, напишите функцию, которая принимает на вход URL и имя класса элемента и
возвращает список из текстов выбранных элементов.
Например: ("https://www.example.com/news", "cell-list__item") -> [
"В Туве семерых человек спасли из реки с сильным течением",
"Панда Катюша вышла на прогулку в уличный вольер",
"Казахстанский миллиардер купил английский футбольный клуб",
]
'''


import requests
from bs4 import BeautifulSoup


def extract_text_by_class(url, class_name):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    elements = soup.find_all(class_=class_name)
    return [element.get_text().strip() for element in elements]


url_ex = "https://htmlacademy.ru/blog/html/class"  # "https://www.example.com/news"   # сайт не работает
# взял первый попавшийся сайт для пример  https://htmlacademy.ru/blog/html/class
class_name_ex = "modal__header" # "cell-list__item"
# взял класс из F12 чтобы понимать , что он есть там: modal__header

print(extract_text_by_class(url_ex, class_name_ex))

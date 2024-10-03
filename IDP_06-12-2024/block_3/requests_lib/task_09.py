# -*- coding: utf-8 -*-

"""
Переработайте задачу 8 используя сессию.

8. Напишите функцию, которая принимает на вход число N, сохраняет N разных фотографий котиков в рабочей директории и
возвращает время работы в секундах. URL для запроса: https://api.thecatapi.com/v1/images/search
"""


import requests
import time
import os


def get_tinme_work_save_images_with_session(n):
    start_time = time.time()
    session = requests.Session()
    for i in range(n):
        response = session.get('https://api.thecatapi.com/v1/images/search')
        if response.status_code == 200:
            img_url = response.json()[0]['url']
            img_data = session.get(img_url).content
            img_num = 0
            img_num += 1
            img_name = "img_{}.png".format(img_num)
            with open(img_name, 'wb') as handler:
                handler.write(img_data)
    end_time = time.time()
    return end_time - start_time


time_1 = get_tinme_work_save_images_with_session(7)
print("Время работы: {} секунд".format(time_1))
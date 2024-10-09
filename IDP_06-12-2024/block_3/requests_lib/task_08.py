# -*- coding: utf-8 -*-

"""
Напишите функцию, которая принимает на вход число N, сохраняет N разных фотографий котиков в рабочей директории и
возвращает время работы в секундах. URL для запроса: https://api.thecatapi.com/v1/images/search
"""


import requests
import time


def get_tinme_work_save_images(n):
    start_time = time.time()
    for i in range(n):
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        if response.status_code == 200:
            image = response.json()[0]['url']
            img_data = requests.get(image).content
            img_num = 0
            img_num += 1
            img_name = "img_{}.png".format(img_num)
            with open(img_name, 'wb') as handler:
                handler.write(img_data)
    end_time = time.time()
    return end_time - start_time


time_1 = get_tinme_work_save_images(7)
print("Время работы: {} секунд".format(time_1))
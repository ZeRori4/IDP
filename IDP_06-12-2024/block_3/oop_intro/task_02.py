# -*- coding: utf-8 -*-

'''
Создайте класс Car с атрибутами manufacturer, model и year. Реализуйте метод get_info, который возвращает описание
машины в формате словаря.
'''


class Car:
    manufacturer = "mazda"
    model = "rx8"
    year = 2

    def get_info(self):
        return {
            "manufacturer": self.manufacturer,
            "model": self.model,
            "year": self.year,
        }


car = Car()

print(car.get_info())

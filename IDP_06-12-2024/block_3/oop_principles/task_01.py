# -*- coding: utf-8 -*-

'''
Создайте класс Animal с методом speak, который возвращает строку "animal speaks". Создайте класс Cat (принимает имя при
инициализации), который наследуется от Animal и переопределяет метод speak так, чтобы возвращалась строка "Meow".
Сделайте имя защищенным атрибутом.
'''


class Animal():
    def speak(self):
        return "animal speaks"


class Cat(Animal):
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow"


animal = Animal()
print(animal.speak())

cat = Cat("Tom")
print(cat.speak())

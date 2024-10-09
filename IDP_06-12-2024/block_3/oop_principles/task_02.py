# -*- coding: utf-8 -*-

'''
Создайте класс Dog, который наследуется от Animal, принимает имя при инициализации и переопределяет метод speak, чтобы
возвращалась строка "Wouf". Добавьте возможность прогулки для класса Dog. Для этого добавьте метод walk (должен
возвращать строку “I'm walking”). Сделайте имя защищенным атрибутом. Оформить как отдельную задачу. Без импорта из
другой задачи.
'''


class Animal:
    def speak(self):
        raise "animal speaks"


class Dog(Animal):
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Wouf"

    def walk(self):
        return "I'm walking"


dog = Dog("Pancho")
print(dog.speak())
print(dog.walk())

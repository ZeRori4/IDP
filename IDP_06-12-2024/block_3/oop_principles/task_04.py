# -*- coding: utf-8 -*-

'''
Добавьте в классы Dog и Cat геттеры и сеттеры для имени питомцев. Все защищенные объекты сделайте приватными.
Оформить как отдельную задачу. Без импорта из другой задачи.
'''


class Animal:
    def speak(self):
        return "animal speaks"


class Cat(Animal):
    def __init__(self, name):
        self.__name = name

    def speak(self):
        return "Meow"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name


class Dog(Animal):
    def __init__(self, name):
        self.__name = name

    def speak(self):
        return "Wouf"

    def walk(self):
        return "I'm walking"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name


cat = Cat("Tom")
print(cat.speak())
print(cat.name)

dog = Dog("Pancho")
print(dog.speak())
print(dog.walk())
print(dog.name)

cat.name = "Dusya"
dog.name = "Rex"
print(cat.name)
print(dog.name)

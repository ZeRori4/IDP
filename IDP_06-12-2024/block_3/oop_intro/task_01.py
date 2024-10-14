# -*- coding: utf-8 -*-

'''
Создайте класс Person с атрибутами name и age. Реализуйте метод greet, который возвращает строку приветствия вида
“Привет, Иван!”.
'''


class Person:
    name = "Ivan"
    age = 30

    def greet(self):
        return "Привет, {}!".format(self.name)


person = Person()

print(person.greet())

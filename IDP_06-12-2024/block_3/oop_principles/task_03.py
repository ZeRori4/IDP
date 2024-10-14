# -*- coding: utf-8 -*-

'''
Реализуйте класс Parrot, который наследуется от Animal и переопределяет метод speak, чтобы он принимал текст, который
говорит животное. Также добавьте метод, отвечающий за полет (должен возвращать строку “I fly”). Сделайте имя и метод
полета защищенными. Оформить как отдельную задачу. Без импорта из другой задачи.
'''


class Animal:
    def speak(self):
        raise "animal speaks"


class Parrot(Animal):
    def __init__(self, name):
        self._name = name

    def speak(self, text):
        return "{} says: {}".format(self._name, text)

    def _fly(self):
        return "I fly"


parrot = Parrot("Rosella")
print(parrot.speak("Кошка Дуся!"))
print(parrot._fly())

# -*- coding: utf-8 -*-

'''
Переработайте код задачи 3, используя концепцию генератора, чтобы он стал проще, но функциональность при этом
сохранилась. Оформите в виде отдельной задачи. Без импорта из другой задачи.
'''


import random


class EvenUpperBoundError(Exception):
    pass


class OddRandomNumbers:
    def __init__(self, limit, upper_bound):
        if upper_bound % 2 == 0:
            raise EvenUpperBoundError("Верхняя граница должна быть нечетным числом.")
        self.limit = limit
        self.upper_bound = upper_bound
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        self.count += 1
        while True:
            number = random.randint(1, self.upper_bound)
            if number % 2 != 0:
                return number


odd_numbers = OddRandomNumbers(5, 15)
for num in odd_numbers:
    print(num)

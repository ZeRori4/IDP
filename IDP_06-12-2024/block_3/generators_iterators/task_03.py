# -*- coding: utf-8 -*-

'''
Реализуйте класс итератор OddRandomNumbers, который принимает лимит (столько чисел нужно сгенерировать) и верхнюю
границу случайного числа. Если верхняя граница является чётным числом, выбрасывайте ошибку EvenUpperBoundError.
На каждой итерации генератора пользователь должен получать нечетное рандомное число от единицы до верхней границы.
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

    def next(self):
        if self.count >= self.limit:
            raise StopIteration
        odd_number = random.randint(1, (self.upper_bound + 1) // 2) * 2 - 1
        self.count += 1
        return odd_number


odd_numbers = OddRandomNumbers(5, 9)
for number in odd_numbers:
    print(number)

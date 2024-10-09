# -*- coding: utf-8 -*-

'''
Реализуйте класс итератор RandomNumbers, который будет принимать лимит (столько чисел нужно сгенерировать) и верхнюю
границу случайного числа. На каждой итерации генератора пользователь должен получать рандомное число от нуля до верхней
границы.
'''


import random


class RandomNumbers():
    def __init__(self, limit, upper_bound):
        self.limit = limit
        self.upper_bound = upper_bound
        self.count = 0

    def __iter__(self):
        return self

    def next(self):
        if self.count < self.limit:
            self.count += 1
            return random.randint(0, self.upper_bound)
        else:
            raise StopIteration()


limit = 5
upper_bound = 10
random_numbers = RandomNumbers(limit, upper_bound)

for number in random_numbers:
    print(number)

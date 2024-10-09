# -*- coding: utf-8 -*-

'''
Реализуйте класс итератор, который будет принимать лимит (столько чисел нужно сгенерировать). На каждой итерации
генератора пользователь должен получать числа из последовательности Фибоначчи.
'''


class FibonacciIterator(object):
    def __init__(self, limit):
        self.limit = limit
        self.count = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def next(self):
        if self.count < self.limit:
            current = self.a
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return current
        else:
            raise StopIteration()


limit = 10
fib_iterator = FibonacciIterator(limit)

for number in fib_iterator:
    print(number)

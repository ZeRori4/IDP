# -*- coding: utf-8 -*-

"""
Переработайте код задачи 5, используя концепцию генератора, чтобы он стал проще, но функциональность при этом
сохранилась. Оформите в виде отдельной задачи. Без импорта из другой задачи.
"""


def fibonacci_generator(limit):
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b


limit = 10
for number in fibonacci_generator(limit):
    print(number)

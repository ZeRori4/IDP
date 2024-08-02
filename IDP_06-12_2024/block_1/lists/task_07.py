# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход целые числа x и y и возвращает
список простых чисел в диапазоне от x до y включительно. Если x > y, то
поменяйте их порядок.
'''


def get_primes(x, y):
    primes = []
    start = min(x, y)
    end = max(x, y)
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes


x1 = 1
y1 = 10

print(get_primes(x1, y1))

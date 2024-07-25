# -*- coding: utf-8 -*-

'''
Реализуйте функцию, которая принимает на вход список чисел, очищает его от
простых чисел и возвращает минимальный и максимальный элементы очищенного
списка.
'''


def get_min_max_without_primes(numbers):
    list_primes = []
    for num in numbers:
        is_prime = True
        if num < 2:   #  num > 1
            is_prime = False
        else:
            for i in range(2, int(num)):
                if (num % i) == 0:
                    is_prime = False
                    break
        if is_prime:
            list_primes.append(num)
    if list_primes:
        return min(list_primes), max(list_primes)


list_numb_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(get_min_max_without_primes(list_numb_1))


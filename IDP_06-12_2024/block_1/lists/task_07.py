# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход целые числа x и y и возвращает
список простых чисел в диапазоне от x до y включительно. Если x > y, то
поменяйте их порядок.
'''


def get_primes(x, y):
    primes = []
    if x < y:
        for num in range(x, y + 1):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    primes.append(num)
        return primes
    else:
        for num in range(y, x + 1):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    primes.append(num)
        return primes


#
# def get_range_primes(x, y):
#     if x < y:
#         primes = []
#         if x > 1:
#             for i in range(2, (x//2)+1):
#                 if (num % i) == 0:
#                     break
#             else:
#                 primes.append(num)
#
#
#         return [i for i in range(x, y+1)]
#     else:
#         return [i for i in range(y, x+1)]


x1 = 1
y1 = 10

print(get_primes(x1, y1))
#
#
# num = 11
# # If given number is greater than 1
# if num > 1:
#     # Iterate from 2 to n // 2
#     for i in range(2, (num//2)+1):
#         # If num is divisible by any number between
#         # 2 and n / 2, it is not prime
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")
# -*- coding: utf-8 -*-

'''
Реализуйте функцию, которая принимает число, являющееся налоговым вычетом, и неизвестное количество аргументов,
являющихся ценами на товары. Функция возвращает среднюю цену с учетом налогового вычета. (13, 1000, 2000, 3000) -> 1740
'''


def get_avg_price_with_deduction(deduction, *prices):
    return int((sum(prices) / len(prices)) - ((sum(prices) / len(prices)) * (deduction * 0.01)))


deduction_1 = 13
prices_1 = [1000, 2000, 3000]

print(get_avg_price_with_deduction(deduction_1, *prices_1))

# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает налоговый вычет в качестве обязательного аргумента, неизвестное количество
аргументов, являющихся ценами на товары, и ключевые аргументы: год, за который производились траты (по умолчанию 2024),
и имя сотрудника, к которому эти траты относятся (по умолчанию 'Employee').
Функция возвращает строку, в которой отражена средняя цена с учетом налогового вычета.
(13, 1000, 2000, 3000) -> 'Результат за 2024 год, для Employee: 1740'

'''


def get_str_result_avg_price_with_deduction(deduction,  *prices, **kwargs):
    year = kwargs.get("year", 2024)
    employee = kwargs.get("employee", "Employee")
    avg_price = (sum(prices) / len(prices)) - ((sum(prices) / len(prices)) * (deduction * 0.01))
    return "Результат за {} год, для {}: {}".format(year, employee, int(avg_price))


deduction_1 = 13
prices_1 = [1000, 2000, 3000]

print(get_str_result_avg_price_with_deduction(deduction_1, *prices_1, employee="Bill", year=2023))

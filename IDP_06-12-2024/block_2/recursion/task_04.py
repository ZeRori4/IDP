# -*- coding: utf-8 -*-

'''
Дана структура (Приложение 1).
Реализуйте функцию, которая умеет работать с подобного рода вложенными структурами. Первым аргументом принимает
структуру, вторым - ключ, значение которого нужно найти. Используя рекурсивный подход, найдите и верните первое
найденное значение, соответствующее ключу.
(site, 'a') -> 'Вверх'
Приложение 1

site = {

    'html': {

        'head': {

            'title': 'Битрикс24',

        },

        'body': {

            'h1': 'Новости',

            'div': 'Поиск',

            'p': ‘Весенний шахматный турнир начался',

            'a': 'Вверх'

        }

    }

}
'''


def find_value(data, key):
    if isinstance(data, dict):
        if key in data:
            return data[key]
        for value in data.values():
            result = find_value(value, key)
            if result is not None:
                return result
    return None


site = {
    'html': {
        'head': {
            'title': 'Битрикс24',
        },
        'body': {
            'h1': 'Новости',
            'div': 'Поиск',
            'p': 'Весенний шахматный турнир начался',
            'a': 'Вверх'
        }
    }
}

result = find_value(site, 'a')
print(result)

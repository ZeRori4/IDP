# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает от пользователя непустой список чисел и возвращает их среднее значение.
Прежде чем брать среднее, провалидируйте элементы списка. Выбрасывайте ошибку, если элемент не является числом.
Если исключения не было, верните среднее значение всех чисел. Если ошибка была, верните среднее значение чисел,
которые были обработаны до ее возникновения.
'''


def avg_list_numbers(lst):
    try:
        avg_list = []
        for num in lst:
            if isinstance(num, (int, float)):
                avg_list.append(int(num))
            else:
                raise TypeError
    except (ValueError, TypeError):
        print("Объект - {} не число".format(num))
    print(sum(avg_list) / len(avg_list))


list_numbers = [4, 2, 23, 34, 23, "d", 2, 4, 2, 9, 133]

avg_list_numbers(list_numbers)

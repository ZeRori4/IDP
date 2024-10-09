# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход два объекта и возвращает результат их конкатенации.
Если по какой-то причине не удалось объединить объекты, выбрасывайте кастомное исключение ConcatenationError
(должно наследоваться от Exception).
'''


class ConcatenationError(Exception):
    def __init__(self, obj1, obj2):
        self.obj1 = obj1
        self.obj2 = obj2

    def __str__(self):
        return "Недопустимое значение: {} или {} ".format(self.obj1, self.obj2)


def concatenate_objects(obj1, obj2):
    try:
        if isinstance(obj1, (str, list)) and isinstance(obj2, (str, list)):
            return obj1 + obj2
        else:
            raise ConcatenationError("Оба объекта должны быть одинакового типа.")
    except Exception as e:
        raise ConcatenationError("Ошибка конкатенации: {}".format(e))


obj_str1 = "asd"
obj_str2 = 123


print(concatenate_objects(obj_str1, obj_str2))

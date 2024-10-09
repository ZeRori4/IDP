# -*- coding: utf-8 -*-

"""
Создайте свой класс CustomString, который наследуется от класса str и переопределяет метод replace, чтобы по умолчанию
он заменял все пробелы на символ подчеркивания.
"""


class CustomString(str):
    def replace(self, old, new=None, count=-1):
        if old == ' ':
            new = '_'
        result = ""
        start = 0
        while True:
            index = self.find(old, start)
            if index == -1 or (count == 0):
                result += self[start:]
                break
            result += self[start:index]
            result += new
            start = index + len(old)
            if count > 0:
                count -= 1
        return CustomString(result)


custom_str = CustomString("QWE-QWE qwe_qwe")
print(custom_str.replace(" ", "-"))
print(custom_str.replace(" ", ""))
print(custom_str.replace("QWE", "ASD"))

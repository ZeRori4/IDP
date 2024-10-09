# -*- coding: utf-8 -*-

'''
Реализуйте свой класс CustomList, который наследуется от класса list и переопределяет метод pop, чтобы он удалял и
возвращал элемент с индексом -1, если переданного индекса нет в диапазоне.
'''


class CustomList(list):
    def pop(self, index=-1):
        if index < -len(self) or index >= len(self):
            index = -1
        element = list.__getitem__(self, index)
        del self[index]
        return element


my_list = CustomList([1, 2, 3, 4, 5])

#print(my_list.pop(10))

#print(my_list.pop(-2))

print(my_list.pop())
print(my_list.pop())
print(my_list.pop())
print(my_list.pop())

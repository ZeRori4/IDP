# -*- coding: utf-8 -*-

'''
Напишите функцию, которая реализует бинарный поиск элемента в отсортированном списке чисел с помощью рекурсии.
Возвращает в качестве результата индекс искомого элемента в списке. В качестве аргументов принимает список чисел и
искомый элемент.
'''


def binary_search(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)


numbers = [1, 3, 5, 7, 9, 11, 13]
index = binary_search(numbers, 7)
print(index)

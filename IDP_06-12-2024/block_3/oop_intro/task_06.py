# -*- coding: utf-8 -*-

'''
Реализуйте класс Student с полями ID, Full name, Group number, Performance. Реализуйте функцию, которая создает список
из десяти студентов (данные о студентах можно придумать), сортирует список по возрастанию среднего балла (Performance)
и возвращает полученный список.
'''


import random


class Student:
    def __init__(self, student_id, full_name, group_number, performance):
        self.student_id = student_id
        self.full_name = full_name
        self.group_number = group_number
        self.performance = performance

    def __repr__(self):
        return "{} (ID: {}, Group: {}, Performance: {})".format(
            self.full_name, self.student_id, self.group_number, self.performance)


def create_students_list():
    students = []
    names = [
        "Иванов Иван", "Петров Петр", "Сидоров Сидор",
        "Кузнецов Алексей", "Смирнова Анна",
        "Попова Мария", "Лебедев Сергей",
        "Ковалев Дмитрий", "Федорова Ольга",
        "Зайцева Наталья"
    ]

    for i in range(10):
        student_id = i + 1
        full_name = names[i]
        group_number = random.randint(1, 5)
        performance = round(random.uniform(2.0, 5.0), 2)
        students.append(Student(student_id, full_name, group_number, performance))
    students.sort(key=lambda student: student.performance)
    return students


for student in create_students_list():
    print(student)

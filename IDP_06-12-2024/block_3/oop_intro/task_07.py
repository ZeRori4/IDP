# -*- coding: utf-8 -*-

"""
Объедините задачи 5 и 6, чтобы класс University принимал объект Student. Оформить как отдельную задачу. Без импорта из
другой задачи.
"""


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


class University:
    def __init__(self, name):
        self.name = name
        self.students = []

    def enroll_student(self, student):
        self.students.append(student)

    def get_numb_of_students_in_university(self):
        return "University {}, {} students.".format(self.name, len(self.students))


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
        group_number = (i % 5) + 1
        performance = round(random.uniform(2.0, 5.0), 2)
        students.append(Student(student_id, full_name, group_number, performance))

    students.sort(key=lambda student: student.performance)
    return students


university = University("МГУ")
students_list = create_students_list()

for student in students_list:
    university.enroll_student(student)

print(university.get_numb_of_students_in_university())

for student in university.students:
    print(student)

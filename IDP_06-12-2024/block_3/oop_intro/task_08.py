# -*- coding: utf-8 -*-

"""
Доработайте класс University, добавив метод get_student, который будет возвращать объект Student по его личному
идентификатору. Также добавьте метод remove, который удаляет студента из университета по его личному идентификатору.
Оформить как отдельную задачу. Без импорта из другой задачи.
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
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def remove(self, student_id):
        for i, student in enumerate(self.students):
            if student.student_id == student_id:
                del self.students[i]
                return True
        return False
    def create_students_list(self):
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
            self.add_student(Student(student_id, full_name, group_number, performance))

    def sort_students_by_performance(self):
        self.students.sort(key=lambda student: student.performance)



university = University()
university.create_students_list()
university.sort_students_by_performance()

print("Список студентов:")
for student in university.students:
    print(student)


student_id_to_find = 3
found_student = university.get_student(student_id_to_find)
print("\nНайденный студент:", found_student)

student_id_to_remove = 5
print("\nСтудент с ID {} был удален.".format(student_id_to_remove))


print("\nОбновленный список студентов:")
for student in university.students:
    print(student)

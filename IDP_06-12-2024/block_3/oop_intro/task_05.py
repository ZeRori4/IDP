# -*- coding: utf-8 -*-

'''
Создайте класс University с атрибутами name и students. Добавьте метод enroll_student, который будет добавлять студента
(имя в строковом формате) в список студентов университета. Если мы решим вывести University на печать, должны получать
название университета и число его студентов: University Name, 15 students.
'''


class University:
    def __init__(self, name):
        self.name = name
        self.students = []

    def enroll_student(self, student_name):
        self.students.append(student_name)

    def get_numb_of_students_in_university(self):
        return "University {}, {} students.".format(self.name, len(self.students))


university = University("МГУ")
university.enroll_student("Алёша")
university.enroll_student("Пётр")

print(university.get_numb_of_students_in_university())

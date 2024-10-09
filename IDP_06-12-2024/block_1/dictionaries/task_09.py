# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход информацию о студентах
(Приложение 2) и название предмета и возвращает список имен студентов, которые
изучают этот предмет, отсортированный по баллу за этот предмет - от меньшего к
большему.
students = {
    student_1: {'name': 'Коля', 'biology': 4.0, informatics: 5.0},
    student_2: {'name': 'Ваня', 'biology': 3.5, chemistry: 3.5},
    student_3: {'name': 'Дима', 'informatics': 4.3, physics: 2.0},
    student_4: {'name': 'Саша', 'maths': 4.2, informatics: 3.0},
}
'''



def get_students_subject(students, subject):
    sort_students = []
    for student in students.values():
        if subject in student:
            sort_students.append((student['name'], student[subject]))
    sort_students.sort(key=lambda item: item[1])
    return [name for name, _ in sort_students]


students_dict = {
    "student_1": {'name': "Kolay", "biology": 4.0, "informatics": 5.0},
    "student_2": {'name': "Vano", "biology": 3.5, "chemistry": 3.5},
    "student_3": {'name': "Dima", "informatics": 4.3, "physics": 2.0},
    "student_4": {'name': "Sasha", "maths": 4.2, "informatics": 3.0},
}

print(get_students_subject(students_dict, "biology"))

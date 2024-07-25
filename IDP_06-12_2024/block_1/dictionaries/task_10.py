# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает на вход информацию о студентах
(Приложение 2) и возвращает словарь, где ключами являются предметы, а
значениями - записи о студентах, которые изучают этот предмет:
{
    biology: {
        student_x: {'name': 'A', 'biology': 4.0, informatics: 5.0},
        student_y: {'name': 'B', 'biology': 4.5, chemistry: 5.0},
        ...
    },
    ...
}
students = {
    student_1: {'name': 'Коля', 'biology': 4.0, informatics: 5.0},
    student_2: {'name': 'Ваня', 'biology': 3.5, chemistry: 3.5},
    student_3: {'name': 'Дима', 'informatics': 4.3, physics: 2.0},
    student_4: {'name': 'Саша', 'maths': 4.2, informatics: 3.0},
}
'''


def group_students_by_subjects(students):
    subjects = {}
    for student_key, student_info in students.items():
        for subject, grade in student_info.items():
            if subject != 'name':
                if subject not in subjects:
                    subjects[subject] = {}
                subjects[subject][student_key] = student_info
    return subjects

students_dict = {
    "student_1": {'name': "Kolay", "biology": 4.0, "informatics": 5.0},
    "student_2": {'name': "Vano", "biology": 3.5, "chemistry": 3.5},
    "student_3": {'name': "Dima", "informatics": 4.3, "physics": 2.0},
    "student_4": {'name': "Sasha", "maths": 4.2, "informatics": 3.0},
}

print(group_students_by_subjects(students_dict))

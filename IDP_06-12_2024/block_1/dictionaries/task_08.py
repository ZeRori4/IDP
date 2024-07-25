# -*- coding: utf-8 -*-

"""
Напишите функцию, которая принимает на вход информацию о студентах
(Приложение 2) и действительное число x и возвращает список имен студентов, у
которых средний балл выше x, отсортированный по среднему баллу - от большего к
меньшему.
students = {
    student_1: {'name': 'Коля', 'biology': 4.0, informatics: 5.0},
    student_2: {'name': 'Ваня', 'biology': 3.5, chemistry: 3.5},
    student_3: {'name': 'Дима', 'informatics': 4.3, physics: 2.0},
    student_4: {'name': 'Саша', 'maths': 4.2, informatics: 3.0},
}
"""


def get_students_avg_score(students, threshold):
    sort_students = []
    for student in students.values():
        grades = [grade for subject, grade in student.items() if subject != 'name']
        name = student['name']
        average_score = sum(grades) / len(grades)
        if average_score > threshold:
            sort_students.append((name, average_score))
    sort_students.sort(key=lambda item: item[1], reverse=True)
    return [name for name, average in sort_students]


students_dict = {
    "student_1": {'name': "Kolay", "biology": 4.0, "informatics": 5.0},
    "student_2": {'name': "Vano", "biology": 3.5, "chemistry": 3.5},
    "student_3": {'name': "Dima", "informatics": 4.3, "physics": 2.0},
    "student_4": {'name': "Sasha", "maths": 4.2, "informatics": 3.0},
}

print(get_students_avg_score(students_dict, 3))

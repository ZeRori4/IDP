# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает информацию о пользователе отдельными аргументами: имя пользователя, адрес
электронной почты, возраст. Провалидируйте переданные аргументы в соответствии с критериями:
        ◦ присутствуют все три поля,
        ◦ имя содержит только буквы,
        ◦ эл. почта содержит @ и точку,
        ◦ возраст представляет собой число от 10 до 99.
В случае ошибки выбрасывайте ValueError с информацией о том, в каком поле ошибка.
'''

#
# def validate_questionnaire(name, email, age):
#     assert name and email and age, "Не все поля заполнены!"
#     assert name.isalpha(), "Имя должно быть только из букв!"
#     assert email.rindex("@") and email.rindex("."), "E-mail должен содержать '@' и '.'!"
#     assert isinstance(age, int) and (10 < age < 99), "Возраст должен быть числом от 10 до 99."
#     try:
#         print("Данные анкеты:\n {}\n {}\n {}".format(name, email, age))
#     except ValueError as e:
#         print("Ошибка: {}".format(e))
#
#
# validate_questionnaire('Anton', 'Anton@mail.ru', 31)


def validate_questionnaire(name, email, age):
    if not (name and email and age):
        raise ValueError("Не все поля заполнены!")
    if not name.isalpha():
        raise ValueError("Имя должно быть только из букв!")
    if "@" not in email or "." not in email:
        raise ValueError("E-mail должен содержать '@' и '.'!")
    if not isinstance(age, int) or not (10 < age < 99):
        raise ValueError("Возраст должен быть числом от 10 до 99")
    return name, email, age


try:
    print("{}".format(validate_questionnaire('Anton', 'Anton@mail.ru', 31)))
except ValueError as e:
    print("Ошибка: {}".format(e))

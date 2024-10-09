# -*- coding: utf-8 -*-

'''
Создайте класс Employee с атрибутами name и salary. Напишите метод increase_salary(N), который увеличивает зарплату на N%.
'''


class Employee:
    name = "Ivan"
    salary = 50000

    def increase_salary(self, percent):
        return self.salary + (self.salary * percent / 100)


employee = Employee()
n = 10

print(employee.increase_salary(n))

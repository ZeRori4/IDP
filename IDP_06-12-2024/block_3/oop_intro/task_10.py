# -*- coding: utf-8 -*-

'''
Реализуйте модель Человек и модель Дом. У человека есть имя и степень сытости (изначально 50, максимум 100).
Человек может:
        ◦ есть (сытость +5, количество еды -5),
        ◦ работать (сытость -5, количество денег +10),
        ◦ играть (сытость -5),
        ◦ ходить в магазин за едой (количество еды +20, количество денег -20),
        ◦ прожить один день (выбирает 2 действия согласно приоритету).
Дом содержит:
        ◦ холодильник с едой (изначально 50 еды)
        ◦ тумбочка с деньгами (изначально 0 денег)
Если сытость человека становится меньше нуля, он умирает. Денег не может быть меньше 0. Логика действий человека:
        1. Генерируется случайное число от 1 до 6.
        2. Если сытость меньше 20 и есть еда хотя бы на один прием пищи, он должен поесть.
        3. Иначе, если еды в доме меньше 10 и есть деньги хотя бы на один поход в магазин, он должен сходить в магазин.
        4. Иначе, если денег в доме меньше 50, он должен работать.
        5. Иначе, если сгенерировано число 1, он должен работать.
        6. Иначе, если сгенерировано число 2, он должен поесть.
        7. Иначе он должен играть.
Укажите при инициализации Человека его индивидуальные особенности (зарплата в день, сколько съедает за раз,
восприимчивость к различным действиям), чтобы, изменяя эти параметры, видеть, как меняется шанс человека прожить нужный
период времени.
Запуск симуляции должен быть выполнен в отдельной функции, которая принимает число дней жизни. Результат можно вернуть
в булевом формате (выжил или нет). Также в файле в рабочей директории должен сохраняться подробный отчет по выживанию.
Где будет информация за каждый день в формате:
День 1: Иван. Действия за день: играть, есть. Сытость 50, деньги 0.
Сытость и деньги в отчёте вычисляются на момент окончания дня.
Попробуйте смоделировать жизнь одного человека в течение года.
'''
import random


class Person:
    def __init__(self, name, salary_per_day, food_consumption, sensitivity):
        self.name = name
        self.hunger = 50
        self.max_hunger = 100
        self.salary_per_day = salary_per_day
        self.food_consumption = food_consumption
        self.sensitivity = sensitivity

    def eat(self, house):
        if house.food >= self.food_consumption:
            house.food -= self.food_consumption
            self.hunger += 5
            if self.hunger > self.max_hunger:
                self.hunger = self.max_hunger

    def work(self, house):
        house.money += self.salary_per_day
        self.hunger -= 5

    def play(self):
        self.hunger -= 5

    def go_to_store(self, house):
        if house.money >= 20:
            house.money -= 20
            house.food += 20

    def is_alive(self):
        return self.hunger >= 0


class House:
    def __init__(self):
        self.food = 50
        self.money = 0


def simulate_life(days):
    house = House()
    person = Person(name="Иван", salary_per_day=10, food_consumption=5, sensitivity=1)

    report = []

    for day in range(1, days + 1):
        if not person.is_alive():
            report.append("День {}: {}. Статус: мертв.".format(day, person.name))
            break

        actions = []

        while person.is_alive() and len(actions) < 3:  # Allow up to 3 actions per day
            action_priority = random.randint(1, 6)

            if person.hunger < 20 and house.food >= person.food_consumption:
                person.eat(house)
                actions.append("есть")

            elif house.food < 10 and house.money >= 20:
                person.go_to_store(house)
                actions.append("в магазин")

            elif house.money < 50:
                person.work(house)
                actions.append("работать")

            elif action_priority == 1:
                person.work(house)
                actions.append("работать")

            elif action_priority == 2:
                if house.food >= person.food_consumption:
                    person.eat(house)
                    actions.append("есть")

            else:
                person.play()
                actions.append("играть")

        report.append(
            "День {}: {}. Действия за день: {}. Сытость {}, деньги {}".format(
                day, person.name, ', '.join(actions), person.hunger, house.money
            )
        )

    with open("survival_report.txt", "w") as file:
        for line in report:
            file.write(line + "\n")

    return person.is_alive()


survived = simulate_life(365)
print("Модель жизни человека в течении года ")

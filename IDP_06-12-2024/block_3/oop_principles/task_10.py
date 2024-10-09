# -*- coding: utf-8 -*-

'''
Напишите классы Круг, Прямоугольник и Треугольник, которые наследуются от GeometricFigure с переопределенным методом
расчёта периметра. Для каждого из классов дополните __str__. Оформить как отдельную задачу. Без импорта из другой задачи.
'''


import math


class GeometricFigure:
    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)

    def __str__(self):
        return "GeometricFigure with sides: {}".format(self.sides)

    def __repr__(self):
        return "GeometricFigure({})".format(self.sides)


class Circle(GeometricFigure):
    def __init__(self, radius):
        self.radius = radius
        GeometricFigure.__init__(self, [2 * math.pi * radius])

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return "Circle with radius: {}".format(self.radius)


class Rectangle(GeometricFigure):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        GeometricFigure.__init__(self, [width, height, width, height])

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return "Rectangle with width: {} and height: {}".format(self.width, self.height)


class Triangle(GeometricFigure):
    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]
        GeometricFigure.__init__(self, self.sides)

    def perimeter(self):
        return sum(self.sides)

    def __str__(self):
        return "Triangle with sides: {}".format(self.sides)


circle = Circle(6)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4, 5)

print(circle)
print("Circle Perimeter: {}".format(circle.perimeter()))
print(rectangle)
print("Rectangle Perimeter: {}".format(rectangle.perimeter()))
print(triangle)
print("Triangle Perimeter: {}".format(triangle.perimeter()))

# -*- coding: utf-8 -*-

"""
Создайте класс GeometricFigure с методом расчёта периметра. Реализуйте __str__ и __repr__ для класса.
"""


class GeometricFigure:
    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)

    def __str__(self):
        return "GeometricFigure with sides: {}".format(self.sides)

    def __repr__(self):
        return "GeometricFigure({})".format(self.sides)


hexagon = GeometricFigure([6, 6, 6, 6, 6, 6])
print(hexagon)
print(repr(hexagon))
print("Perimeter: {}".format(hexagon.perimeter()))

# -*- coding: utf-8 -*-

"""
Требуется разработать класс Matrix для обработки и анализа данных. Ваш класс должен предоставлять функциональность для
выполнения основных операций с матрицами: сложение, вычитание, умножение и транспонирование.
"""


class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def add(self, other):
        result = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def subtract(self, other):
        result = [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def multiply(self, other):
        result = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)) for j in range(other.cols)] for i
                  in range(self.rows)]
        return Matrix(result)

    def transpose(self):
        result = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return Matrix(result)



matrix_a = Matrix([[1, 2, 3], [4, 5, 6]])
matrix_b = Matrix([[7, 8, 9], [10, 11, 12]])

print("Matrix A:")
print(matrix_a)

print("\nMatrix B:")
print(matrix_b)

print("\nA + B:")
print(matrix_a.add(matrix_b))

print("\nA - B:")
print(matrix_a.subtract(matrix_b))

print("\nA * B:")
matrix_c = Matrix([[1, 2], [3, 4], [5, 6]])
print(matrix_a.multiply(matrix_c))

print("\nTransposed A:")
print(matrix_a.transpose())

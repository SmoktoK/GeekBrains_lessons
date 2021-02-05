"""
 Реализовать класс Matrix (матрица). Обеспечить перегрузку
 конструктора класса (метод __init__()), который должен принимать
 данные (список списков) для формирования матрицы.
 Подсказка: матрица — система некоторых математических величин,
 расположенных в виде прямоугольной схемы.
 Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
 Следующий шаг — реализовать перегрузку метода __str__() для
 вывода матрицы в привычном виде.
 Далее реализовать перегрузку метода __add__() для реализации
 операции сложения двух объектов класса Matrix (двух матриц).
 Результатом сложения должна быть новая матрица.
 Подсказка: сложение элементов матриц выполнять
 поэлементно — первый элемент первой строки первой
 матрицы складываем с первым элементом первой строки
 второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, list_1, list_2):
        self.matr = [list_1, list_2]
        self.list_1 = list_1
        self.list_2 = list_2

    def printMatrix_1(self):
        for i in range(len(self.list_1)):
            for j in range(len(self.list_1[i])):
                print(self.list_1[i][j], end=' ')
            print()

    def printMatrix_2(self):
        for i in range(len(self.list_2)):
            for j in range(len(self.list_2[i])):
                print(self.list_2[i][j], end=' ')
            print()

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matr]))

    def __add__(self):
        matr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        for el in range(len(self.list_1)):

            for j in range(len(self.list_2[el])):
                matr[el][j] = self.list_1[el][j] + self.list_2[el][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))


my_matrix = Matrix([[5, 11, 20], [6, 12, 11], [34, 19, 13]], [[24, 36, 2], [6, 7, 8], [2, 5, 41]])

print('Матрица №1')
my_matrix.printMatrix_1()
print('------')
print('Матрица №2')
my_matrix.printMatrix_2()
print('------')
print('Итоговая матрица')
print(my_matrix.__add__())
print('------')
print(my_matrix.__str__())


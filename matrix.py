from random import randint


def main():
    size = int(input('Введите размер матрицы (integer): '))
    end_range = int(input('Введите целочисленный конечный диапазон для матрицы, означающей рандомизацию от 1 до: '))
    matrix1 = rand_matrix(1, end_range, size)
    matrix2 = rand_matrix(1, end_range, size)
    print('Перавая рандомная матрица')
    output(matrix1)
    print()
    print('Вторая рандоманя матрица')
    output(matrix2)
    print()
    print('Результат перемножения: ')
    output(matrix_mul(matrix1, matrix2, size))


def rand_matrix(range_start, range_end, size):
    mat_rand = [[randint(range_start, range_end) for j in range(size)] for i in range(size)]
    return mat_rand


def matrix_mul(input_matrix1, input_matrix2, matrix_size):
    end_matrix = rand_matrix(0, 0, matrix_size)
    if len(input_matrix1) != len(input_matrix2):
        print('Матрицы не равны')
    else:
        size = len(input_matrix1)
        for i in range(size):
            for j in range(size):
                for k in range(size):
                    end_matrix[i][j] += input_matrix1[i][k] * input_matrix2[k][j]

    return end_matrix


def output(matrix):
    for r in matrix:
        print(r)


main()

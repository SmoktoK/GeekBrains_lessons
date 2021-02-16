"""
Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.
"""


def max_num():
    num = 0
    for num in range(3):
        num = (int(input('Введите число: ')))
    nums = [num]
    print('Максимальное значение: ', max(nums))


max_num()

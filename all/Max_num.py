"""
Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.
"""

nums = []
def max_num():
    num = 0
    for num in range(3):
        num = (int(input('Введите число: ')))
        nums.append(num)
    print(nums)
    print('Максимальное значение: ', max(nums))


max_num()

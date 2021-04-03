"""
Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент.
Если список пустой функция должна вернуть None. Проверьте работу функций в этом же модуле
"""
import random


def def_random(input_list):
    if input_list:
        total = random.choice(input_list)
        return total


print(def_random([1, 2, 3, 4]))
print(def_random([]))

"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить
только первые n чисел, начиная с 1! и до n!.
"""

from itertools import count
from math import factorial

n = int(input('Введите число, факториал которого хотите получить: '))
def fgen():
    for i in count(1):
        yield factorial(i)

generator = fgen()
x = 0
for k in generator:
    if x < n:
        print(k)
        x += 1
    else:
        break
"""
Дан список, заполненный произвольными числами. Получить список из элементов исходного, удовлетворяющих следующим условиям:

Элемент кратен 3,
Элемент положительный,
Элемент не кратен 4.
"""


import random
num = int(input('Введите длину списка: '))
print(type(num))
numbers = []

for i in range(0, num):
    len = random.randint(-100, 100)
    numbers.append(len)

print(numbers)

result = [number for number in numbers if number > 0 and number % 3 == 0 and number % 4 != 0]

print(result)

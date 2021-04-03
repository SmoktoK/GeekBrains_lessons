"""
Написать функцию которая принимает на вход число от 1 до 100. Если число равно 13,
функция поднимает исключительную ситуации ValueError иначе возвращает введенное число,
возведенное в квадрат.

Далее написать основной код программы. Пользователь вводит число.
Введенное число передаем параметром в написанную функцию и печатаем результат, который вернула функция.
Обработать возможность возникновения исключительной ситуации, которая поднимается внутри функции.
"""


def unlucky_number(number):
    if number == 13:
        raise ValueError('Несчастливое число!')
    else:
        return number ** 2


number = int(input('Введите число: '))

try:
    result = unlucky_number(number)
except ValueError:
    print('У нас несчастливое число!')
else:
    print(result)

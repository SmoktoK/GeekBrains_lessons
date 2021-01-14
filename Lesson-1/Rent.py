income = int(input('Введите количество выручки фирмы: '))
rate = int(input('Введите расходы фирмы: '))
if income > rate:
    people = int(input('Введите количество сотрудников фирмы: '))
    print('Выручка фирмы больше рассходов!')
    rent = income / rate
    totall = income / people
    print('Рентабельность составила: ', "%.1f" % (rent))
    print('Прибыль фирмы в расчете на 1 сотрудника составила: ', "%.2f" % (totall))

elif income < rate:
    print('Выручка фирмы меньше расходов!')
else:
    print('Выручка фирмы равна расходам')

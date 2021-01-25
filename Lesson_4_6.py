from itertools import count

max_num = int(input('Введите максимальное число: '))
for el in count(int(input('Введите стартовое число: '))):
    if el > max_num:
        break
    else:
        print(el)

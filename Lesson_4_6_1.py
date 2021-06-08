from itertools import cycle

max_num = int(input('Введите максимальное число повторений: '))
c = 1
for el in cycle(('ABC', 123, 1.5, None)):
    if c > max_num:
        break
    c += 1
    print(el)


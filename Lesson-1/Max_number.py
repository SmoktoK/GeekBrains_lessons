num = int(input('Введите число: '))
totall = num % 10
num = num//10
while num > 0:
    if num % 10 > totall:
        totall = num % 10
    num = num // 10
print('Максимальное число: ', totall)
num = None
while True:
    num = int(input('Введите число: '))
    if num <= 0:
        print('Введите положительное число')
    else:
        break
num = str(num)
num2 = num + num
num3 = num + num2
sum = int(num) + int(num2) + int(num3)
print('сумма чисел ', num+'+'+num2+'+'+num3, 'равняется:', sum)


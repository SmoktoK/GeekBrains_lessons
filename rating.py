my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг на данный момент: {my_list}")
num = int(input('Введите число (999 - выход): '))
while num != 999:
    my_list.append(num)
    my_list.sort(reverse=True)
    print(my_list)
    num = int(input('Введите число (999 - выход): '))
print(f"Итоговый список: {my_list}")
my_list = input('введите список: ').split() # Разбиваем список по словам
el = 0
for i in range(int(len(my_list)/2)):
    my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
    el += 2
print(my_list)


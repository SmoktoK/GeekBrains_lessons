def my_func():
    x = int(input('введите первый аргумент:'))
    y = int(input('введите второй аргумент: '))
    z = int(input('введите третий аргумент: '))
    my_list = [x, y, z]
    my_list.sort(reverse=True)
    return my_list

my_list = my_func()
print('максимальное число: ', my_list[0], 'минимальное число: ', my_list[2])
print('сумма наибольших чисел: ', my_list[0] + my_list[1])

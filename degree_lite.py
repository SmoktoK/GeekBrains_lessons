def div():
    try:
        arg1 = int(input('Введите делимое: '))
        arg2 = int(input('Введите делитель: '))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return 'Делить на 0 нельзя!'
    return res


print(f'arg1 / arg2 = {div()}')
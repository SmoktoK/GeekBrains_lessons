"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

my_list = []

while True:
    line = input('Введите данные: ')
    if line == '':
        print(my_list)
        break
    else:
        new_line = line + '\n'
        my_list.append(new_line)

with open('Lesson_5_1_test.txt', 'w') as test_file:
    test_file.writelines(my_list)

with open("Lesson_5_1_test.txt") as f_obj:
    for line in f_obj:
        print(line)

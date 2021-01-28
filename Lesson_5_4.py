"""
Создать (не программно) текстовый файл со следующим содержимым:

One — 1

Two — 2

Three — 3

Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
rus_list = ['Один', 'Два', 'Три', 'Четыре']
i = 0
with open('Lesson_5_4_test.txt') as my_file:
    for el in my_file:
        tot = el.split()
        tot[0] = rus_list[i]
        i += 1
        print(' '.join(tot))
        with open('Lesson_5_4_rus.txt', 'a') as rus_file:
            rus_file.writelines(''.join(tot) + '\n')

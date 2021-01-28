"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

my_line = ['Gamer Simpson\n', 'Hello world\n', 'I love Python very much\n']
with open('Lesson_5_2_test.txt', 'w') as my_file:
    my_file.writelines(my_line)
with open('Lesson_5_2_test.txt') as my_file:
    lines = 0
    letters = 0
    for line in my_file:
        lines += line.count('\n')
        letters = len(line.split())
        print(f'В строке {lines}, количество слов составляет: {letters} ')

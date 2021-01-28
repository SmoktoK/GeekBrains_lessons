"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников
"""
firm = {'Black': 17, 'Smith': 21, 'Potter': 19, 'Green': 15}
try:
    my_file = open('Lesson_5_3_test.txt', 'w')
    for last_name, salary in firm.items():
        my_file.write(last_name + ':' + str(salary) + "\n")
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    my_file.close()
summa = 0
count = 0
persons = []
with open("Lesson_5_3_test.txt") as my_file:
    for line in my_file:
        print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) < 20:
            persons.append(tokens[0])
        summa += int(tokens[1])
        count += 1
result = summa / count
print(f"Сотрудники с окладом менее 20: {persons}")
print(f"Средний оклад в компании составляет: {result}")

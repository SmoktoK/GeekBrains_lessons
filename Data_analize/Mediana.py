# Напишите функцию, которая найдет медиану столбца total_bedrooms из файла 'sample_data/california_housing_test.csv'
# Можно использовать только стандартный python, без pandas, numpy и других продвинутых пакетов

import csv
import statistics

my_list = []

with open("california_housing_test.csv", "r") as test:
    file_reader = csv.reader(test, delimiter=",")
    count = 0
    for row in file_reader:
        if count == 0:
            print('Количество столбцов: ', len(row))
            f = (row.index('total_bedrooms'))
            print('Столбец total_bedrooms является', f, 'по счету.')
        else:
            my_list.append(round(float(row[f])))

        count += 1
    print(f'Всего в файле {count - 1} строк.')


print('Медианой столбца total_bedrooms является:', statistics.median(my_list))

with open("test.txt", "w") as file:
    file.writelines("%s\n" % line for line in my_list)





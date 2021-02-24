import os


def create():
    for i in range(1, 10):
        os.mkdir('dir_' + str(i))


create()
print('Создание каталогов завершено')

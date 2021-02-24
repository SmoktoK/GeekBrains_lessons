import os


def remove():
    for i in range(1, 10):
        os.rmdir('dir_'+str(i))


remove()
print('Каталоги удалены')
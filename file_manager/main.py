import sys
from core import copy_file, create_file, create_folder, delete_file, get_list, save_info

save_info('Start')
command = sys.argv[1]
try:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        name = sys.argv[2]
        create_file(name)
    elif command == 'create_folder':
        name = sys.argv[2]
        create_folder(name)
    elif command == 'delete':
        name = sys.argv[2]
        delete_file(name)
    elif command == 'copy':
        name = sys.argv[2]
        new_name = sys.argv[3]
        copy_file(name, new_name)
    elif command == 'help':
        print('=)')
except IndexError:
    print('Введены не все параметры')


save_info('End')
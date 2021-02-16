"""
Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
name - строка полученная от пользователя,
health = 100,
damage = 50.
### Поэкспериментируйте с значениями урона и жизней по желанию.
### Теперь надо создать функцию attack(person1, person2).
Примечание: имена аргументов можете указать свои.
### Функция в качестве аргумента будет принимать атакующего и атакуемого.
### В теле функция должна получить параметр damage атакующего и отнять это количество
от health атакуемого. Функция должна сама работать со словарями и изменять их значения.
"""

player_name = input('Введите имя героя: ')
player = {'player_n': player_name,
          'health_p': 100,
          'damage_p': 50,
          'armor_p': 2.5}
enemy_name = input('Введите имя Плохого чувака: ')
enemy = {'name_e': enemy_name,
         'health_e': 150,
         'armor_e': 5,
         'damage_e': 15}


def attack(hero, bad_guy):
    hero['health_p'] -= bad_guy['damage_e'] / hero['armor_p']


attack(player, enemy)
print(enemy)

attack(player, enemy)
print(player)

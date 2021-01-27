my_name = input('Введите имя: ')
my_surname = input('Введите фамилию: ')
my_city = input('Введите город: ')
my_email = input('введите email: ')
byear = input('введите год рождения: ')
my_telephone = input('введите номер телефона: ')


def my_func(name, surname, city, email, year, telephone):
    print(name, surname, city, email, year, telephone)


my_func(surname=my_surname, name=my_name, city=my_city, email=my_email, year=byear, telephone=my_telephone)

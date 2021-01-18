my_list = input('Введите строку: ').split()
i = 0
for word in my_list:
    i += 1
    word = word[0:10]
    print(f"{i}. {word}")
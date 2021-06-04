import random
c = 0
my_list = {}

while c < 100:
    a = random.randint(1, 34)
    b = random.randint(1, 10)
    d = random.randint(1, 10)
    print(f'({d},{a},{b}),')
    with open('total', 'a') as f:
        f.writelines(f'({d},{a},{b}),\n')
    c += 1




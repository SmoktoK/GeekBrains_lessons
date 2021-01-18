import value as value

goods_dict = []
goods_list = []
goods_tuple = ()
name = []
price = []
quantity = []
unit = []
#analitic_dict = { 'Название': name, 'Цена': price, 'количество': quantity, 'Ед. измерения': unit}

n_goods = int(input('введите количество наименований товара: '))
i = 1

while i <= n_goods:
    goods_dict = {'Название': input('Введите название товара: '), 'Цена': input('введите цену товара: '),
                  'количество': input('введите количество товара: '),
                  'Ед. измерения': input('введите единицу измерения: ')}
    goods_tuple = (i, goods_dict)
    goods_list.append(goods_tuple)

    name.append(goods_dict.get('Название'))
    price.append(goods_dict.get('Цена'))
    quantity.append(goods_dict.get('количество'))
    unit.append(goods_dict.get('Ед. измерения'))

    i += 1

print('Исходные данные:')
for el in goods_list:
    print(el)

analitic_dict = {'Название': name, 'Цена': price, 'количество': quantity, 'Ед. измерения': unit}
print('Анализ')
for key in analitic_dict.items():
    print(f'"{key}": {value}')
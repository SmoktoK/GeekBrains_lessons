"""
Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
"""


fruits1 = ['apple', 'apricot', 'pineapple', 'banana', 'grapefruit']
fruits2 = ['apple', 'bergamot', 'pineapple', 'avocado', 'grapefruit']

result = []

for fruit in fruits1:
    if fruit in fruits2:
        result.append(fruit)

print(result)

result = [fruit for fruit in fruits1 if fruit in fruits2] # Использование генератора для решения

print(result)

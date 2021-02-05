"""
 Реализовать проект расчета суммарного расхода ткани на
 производство одежды. Основная сущность (класс) этого
 проекта — одежда, которая может иметь определенное название.
 К типам одежды в этом проекте относятся пальто и костюм.
 У этих типов одежды существуют параметры: размер (для пальто)
 и рост (для костюма). Это могут быть обычные числа: V и H,
 соответственно.
 Для определения расхода ткани по каждому типу одежды использовать
 формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
 Проверить работу этих методов на реальных данных.
 Реализовать общий подсчет расхода ткани. Проверить на
 практике полученные на этом уроке знания: реализовать абстрактные
 классы для основных классов проекта, проверить на практике
 работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Textile:

    @abstractmethod
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @abstractmethod
    def coat_fabric(self):
        return self.width / 6.5 * 0.5

    @abstractmethod
    def suit_fabric(self):
        return 2 * self.height + 0.3

    @property
    def fabric_total(self):
        return str(f'Общая площадь ткани составляет {round((self.width / 6.5 * 0.5) + (self.height * 2 + 0.3))}')


class Coat(Textile, ABC):
    def __init__(self, width, height):
        super(Coat, self).__init__(width, height)
        self.coat_fabric = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь пальто составляет: {self.coat_fabric}'


class Suit(Textile, ABC):
    def __init__(self, width, height):
        super(Suit, self).__init__(width, height)
        self.suit = round(2 * self.height + 0.3)

    def __str__(self):
        return f'Площадь костюма составляет:{self.suit}'


textile = Textile(100, 200)
coat = Coat(20, 10)
suit = Suit(20, 10)

print(textile.fabric_total)
print(coat)
print(suit)


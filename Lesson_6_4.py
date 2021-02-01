"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

class Car:
    # Атрибуты класса
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # Методы класа
    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def show_speed(self):
        return f'Текущая скорость {self.name} составляет: {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name} составляет: {self.speed}')

        if self.speed > 60:
            print(f'{self.name} превышает установленную скорость')

        else:
            print(f'{self.name} едет с допустимой скоростью')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name} составляет: {self.speed}')

        if self.speed > 40:
            print(f'{self.name} превышает установленную скорость!')

        else:
            print(f'{self.name} едет с допустимой скоростью')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} полицейская машина'
        else:
            return f'{self.name} не полицейская машина'


audi = SportCar(100, 'Красный', 'Audi', False)
oka = TownCar(30, 'Белый', 'Oka', False)
lada = WorkCar(70, 'Черный', 'Lada', True)
ford = PoliceCar(110, 'Синий', 'Ford', True)
print(lada.turn_left())
print(f'Когда {oka.turn_right()}, {audi.stop()}')
print(f'{lada.go()} со скоростью {lada.show_speed()}')
print(f'Цвет {lada.name}  {lada.color}')
print(f'{audi.name} является полицейской машиной- {audi.is_police}')
print(f'{lada.name} является полицейской машиной- {lada.is_police}')
print(audi.show_speed())
print(oka.show_speed())
print(ford.police())
print(ford.show_speed())

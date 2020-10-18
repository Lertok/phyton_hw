# 1 Светофор

import time


class TrafficLight:
    __color = ()

    def changecolor(self, newcolor):
        self._Tafficlight__color = newcolor


red = TrafficLight()
yellow = TrafficLight()
green = TrafficLight()

red.changecolor('red')
yellow.changecolor('yellow')
green.changecolor('green')

power = input('Хотите запустить светофор? Напишите "on" для запуска: ')

if power == 'on':
    print('Светофор запущен')
else:
    power_01 = input('Вы отказались от запуска, или сделали ошибочный ввод. \nПерезапустить программу? да или нет ')
    if power_01 == 'да':
        power = input('Хотите запустить светофор? Напишите on для запуска: ')
    else:
        print('Вы отказались от запуска светофора!')

while power == 'on':  # не придумал как тут сделать принудительное прерывание цикла, если надо выключить светофор???.
    print(red._Tafficlight__color)
    time.sleep(7)
    print(yellow._Tafficlight__color)
    time.sleep(2)
    print(green._Tafficlight__color)
    time.sleep(5)


# 2 Реализовать класс Road (дорога),
# в котором определить атрибуты: length (длина), width (ширина)

class Road:

    def __init__(self, _lenght, _width):
        self._lenght = _lenght
        self._width = _width

    def asph_mas(self, mass, thik):
        self.mass = mass
        self.thik = thik
        return self._lenght * self._width * self.mass * self.thik


# написал для проверки, через консоль работает
# r = Road(20, 5000)
# print((r.asph_mas(25, 5)))


# 3 Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность), incom(доход).

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            'wage': wage,
            'bonus': bonus,
        }


class Position(Worker):

    def get_full_name(self):
        return f'Имя работника: {self.name} {self.surname}, Должность: {self.position}'

    def get_total_income(self):
        return f"Доход с премией: {self._income['wage'] + self._income['bonus']} рублей"


# написал для проверки, через консоль работает
# p = Position('Ivan', 'Drago', 'Superman', 100, 20)
# print(p.get_full_name())
# print(p.get_total_income())


# 4

class Car:
    def __init__(self, speed, color, name, is_polis):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polis = bool(is_polis)

        print('Машина:', self.name, 'цвет:', self.color, 'скорость:', self.speed)

        if is_polis:
            print('Это ПОЛИЦИЯ')
        else:
            print('Обычная машина')

    def show_speed(self):
        return f'Текущая скорость автомобиля: {self.speed} км/ч'

    def go(self):
        return f'Машина начала движение, Брррррр.....'

    def stop(self):
        return f'Машина остановилась'

    def turn(self, direction):
        self.direction = direction
        if direction == 'left':
            return f'Машина повернула на лево'
        elif direction == 'right':
            return f'Машина повернула на право'
        else:
            return f'Машина продолжает движение'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Текущая скорость автомобиля: {self.speed} км/ч, ВЫ ПРЕВЫСИЛИ СКОРОСТЬ, сбрось до 60 км/ч !!!'
        else:
            return f'Текущая скорость автомобиля: {self.speed} км/ч, Так держать!!!'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Текущая скорость автомобиля: {self.speed} км/ч, ВЫ ПРЕВЫСИЛИ СКОРОСТЬ, сбрось до 40 км/ч !!!'
        else:
            return f'Текущая скорость автомобиля: {self.speed} км/ч, Так держать!!!'


class PoliceCar(Car):
    pass


# 5

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки...')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title}! Здорово, Вы решили порисовать ручкой!')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title}! Воу, да вы любитель карандашей, прихватите ластик!')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title}! Ух ты, рисунок будет ярким!')

# Для проверки
# s = Stationery('')
# p = Pen('Ручка')
# pp = Pencil('Карандаш')
# h = Handle('Маркер')
# s.draw()
# p.draw()
# pp.draw()
# h.draw()

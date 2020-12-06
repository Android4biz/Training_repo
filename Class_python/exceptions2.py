from loguru import logger



class PositiveValueError(ValueError):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return logger.error('error', self.value)


class Car:
    def __init__(self, speed, weight, color, fuel):
        if speed < 0:
            raise PositiveValueError(speed)
        self.speed = speed
        if weight < 0:
            raise PositiveValueError(weight)
        self.weight = weight
        self.color = color
        if fuel < 0:
            raise PositiveValueError(fuel)
        self.fuel = fuel


    def __str__(self):
        return "No Error"


class Plane:
    def __init__(self, range_of_flight, speed, weight, fuel):
        if speed < 0:
            raise PositiveValueError(speed)
        self.speed = speed
        if weight < 0:
            raise PositiveValueError(weight)
        self.weight = weight
        if range_of_flight < 0:
            raise PositiveValueError(range_of_flight)
        self.range_of_flight = range_of_flight
        if fuel < 0:
            raise PositiveValueError(fuel)
        self.fuel = fuel


    def __str__(self):
        return "No Error"


class Motorbike:
    def __init__(self, speed, weight, wheels, fuel):
        if speed < 0:
            raise PositiveValueError(speed)
        self.speed = speed
        if weight < 0:
            raise PositiveValueError(weight)
        self.weight = weight
        if wheels < 0:
            raise PositiveValueError(wheels)
        self.wheels = wheels
        if fuel < 0:
            raise PositiveValueError(fuel)
        self.fuel = fuel

    def __str__(self):
        return "No Error"



try:
    c = Car(300, 1200, 'red', 50)
    p = Plane(800, 550, 10000, 50)
    m = Motorbike(250, 400, 2, 10)
except PositiveValueError as e:
    print('Была ошибка', e)

print(c)
print(p)
print(m)
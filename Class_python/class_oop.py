from abc import ABCMeta, abstractmethod
from loguru import logger
from exceptions2 import PositiveValueError

class Vehicle(metaclass=ABCMeta):
    def __init__(self, weight, speed, fuel):
        self.weight = weight
        self.speed = speed
        self.fuel = fuel

    @abstractmethod
    def speedup(self):
        pass


class Car(Vehicle, metaclass=ABCMeta):
    def __init__(self, speed, weight, color, fuel):
        super().__init__(weight, speed, fuel)
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


    def speedup(self):
        return "Speed up Ford Mustang 0 - 100 km/h: 4.5 s "


    def __str__(self):
        return  f"Auto 'Ford Mustang' Speed: {self.speed} km/h, Weight: {self.weight} kg," \
                f"Color: {self.color}, Fuel: {self.fuel}"



class Plane(Vehicle):
    def __init__(self, range_of_flight, speed, weight, fuel):
        super().__init__(weight, speed, fuel)
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

    def speedup(self):
        return "Speed up Boing 737  0 - 100 km/h: 5 s"

    def __str__(self):
        return f"Boing 737 Range of flight: {self.range_of_flight} km, Speed: {self.speed} km/h,  Weight: {self.weight} kg"\



class Motorbike(Vehicle):
    def __init__(self, speed, weight, wheels, fuel):
        super().__init__(weight, speed, fuel)
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


    def speedup(self):
        return "Speed up motorbike 'Yamaha' 0 - 100 km/h: 4 s"


    def __str__(self):
        return f"Motorbike 'Yamaha' Speed: {self.speed} km/h, Weight: {self.weight} kg," \
               f"Wheels: {self.wheels}"





c = Car(300, 1200, 'red', 50)
p = Plane(800, 550, 10000, 50)
m = Motorbike(250, 400, 2, 10)


print(c)
print(c.speedup())
print(p)
print(p.speedup())
print(m)
print(m.speedup())






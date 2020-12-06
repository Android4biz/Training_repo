from dataclasses import dataclass
from exceptions2 import PositiveValueError



@dataclass
class Datauto:
    year: int
    model: str
    price: int

    def __post_init__(self):
        if self.price < 0:
            raise PositiveValueError(ValueError)


@dataclass
class Datplane:
    year: int
    model: str
    price: int


    def __post_init__(self):
        if self.price < 0:
            raise PositiveValueError(ValueError)


@dataclass
class Datmotorbike:
    year: int
    model: str
    price: int

    def __post_init__(self):
        if self.price < 0:
            raise PositiveValueError(ValueError)


a = Datauto('Ford Mustang', 2020, 3000000)
b = Datplane('Boing 737', 1996, 35000000)
y = Datmotorbike('Yamaha', 2020, 1000000)


print(a)
print(b)
print(y)
from dataclasses import dataclass

@dataclass
class Vehicle:
    make: str
    color: str
    year: int

@dataclass
class Truck(Vehicle):
    weight: float
    length: float


if __name__ == '__main__':
    truck = Truck()

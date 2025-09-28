from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self): pass

    @abstractmethod
    def accelerate(self): pass

    @abstractmethod
    def brake(self): pass

class BMW(Vehicle):
    def start_engine(self): return "BMW engine roars to life!"
    def accelerate(self): return "BMW accelerates smoothly."
    def brake(self): return "BMW brakes with precision."

class Ferrari(Vehicle):
    def start_engine(self): return "Ferrari engine screams awake!"
    def accelerate(self): return "Ferrari launches like a rocket!"
    def brake(self): return "Ferrari brakes with flair."

def test_drive(vehicle):
    print(vehicle.start_engine())
    print(vehicle.accelerate())
    print(vehicle.brake())

test_drive(BMW())
print()
test_drive(Ferrari())
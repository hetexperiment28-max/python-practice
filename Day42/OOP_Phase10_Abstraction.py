#Day 42 - Abstraction
#Vehicle Management System

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start():
        
        pass


class Car(Vehicle):

    def __init__(self, company):
        super().__init__()
        self.company = company


    def start(self):

        print("Car Started")


class Bike(Vehicle):

    def __init__(self, brand):
        super().__init__()
        self.brand = brand

    def start(self):
        print("Bike Sarted")


car = Car("Hyundai")
bike = Bike("Suzuki")

vehicles = [
    car,
    bike
]

for v in vehicles:
    v.start()


from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass
# Child class
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started using key ignition.")

# Child class
class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started using kick or self-start.")
# Child class
class Bus(Vehicle):
    def start_engine(self):
        print("Bus engine started using air brake system.")

car = Car()
bike = Bike()
bus = Bus()

car.start_engine()
bike.start_engine()
bus.start_engine()

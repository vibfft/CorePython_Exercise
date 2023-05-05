# can't create an instance of it

from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass

class Car(Vehicle):
    def go(self):
        print(f"car zooms!")

class Motorcycle(Vehicle):
    def go(self):
        print(f"motorcycle goes!")
        
        

c = Car()
m = Motorcycle()

for v in [c, m]:
    v.go()
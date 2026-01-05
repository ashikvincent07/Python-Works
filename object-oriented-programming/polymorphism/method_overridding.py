"""
Docstring for object-oriented-programming.polymorphism.method_overridding

child class changes the behaviour of parent class method
"""


class Vehicle:
    def __init__(self, brand, title):
        self.brand = brand
        self.title = title

    def move(self):
        print(self.title," is moving")
    
class Car(Vehicle):
    def __init__(self, brand, title):
        super().__init__(brand, title)
    
class Ship(Vehicle):
    def __init__(self, brand, title):
        super().__init__(brand, title)

    def move(self): # Ship changed the behaviour of parent class method " move "
        print(self.title," is sailing")

car_instance = Car("Toyota", "Corrola")
ship_instance = Ship("Royal Caribbean", "Icon of the seas")

car_instance.move()
ship_instance.move()
        
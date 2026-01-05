"""
constructor :
normal method
invoked when creating the object
__init__ is the constructor in python
"""
class Car:
    name:str
    brand:str
    price:int
    color:str

    def set_car(self,name,brand,price,color):
        self.name = name
        self.brand = brand
        self.price = price
        self.color = color

    def display(self):
        print(f"Car name : {self.name}")
        print(f"Brand : {self.brand}")
        print(f"Price : {self.price}")
        print(f"Color : {self.color}")
        print()

car_instance1 = Car()
car_instance2 = Car()

car_instance1.set_car("Defender", "Landrover", 10000000, "white")
car_instance2.set_car("Innova", "Toyota", 1700000, "black")

car_instance1.display()
car_instance2.display()

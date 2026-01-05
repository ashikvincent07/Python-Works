class Parent:
    def car(self):
        print("civic")

class Child(Parent):  # parent class in brackets to achieve inheritance
    def bike(self):
        print("hunter")


child_instance = Child()
child_instance.car()
child_instance.bike()
class GrandParent:

    def properties(self):
        print("80cent land, retro house")

class Parent(GrandParent):

    def vehicles(self):
        print("Porshe, Ninja, S1000")

class Child(Parent):

    def gadgets(self):
        print("Laptop, Speaker, Earpod")

child_instance1 = Child()

child_instance1.gadgets()
child_instance1.vehicles()
child_instance1.properties()
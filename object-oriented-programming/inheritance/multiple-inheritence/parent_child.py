class Father:

    def father_skill(self):
        print("Cricket skill")

class Mother:

    def mother_skill(self):
        print("Cooking skill")

class Child(Father, Mother):

    def child_skill(self):
        print("Gaming skill")


child_instance1 = Child()
child_instance1.child_skill()
child_instance1.father_skill()
child_instance1.mother_skill()
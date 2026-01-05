class Person:
    name : str
    age : int
    gender : str

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @property
    def get_age(self):
        print(self.age)

    @property
    def get_info(self):
        print(self.name)
        print(self.gender)
        print(self.age)

person_instance = Person("Ashik", 21, "male")

person_instance.get_info



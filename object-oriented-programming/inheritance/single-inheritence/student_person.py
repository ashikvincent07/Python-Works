class Person:
    name : str
    gender : str
    age : int

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def display(self):
        print(f"Name: {self.name}  Gender: {self.gender}   Age: {self.age}")

class Student(Person):
    roll_no : int
    course : str

    def __init__(self, name, gender, age, roll_no, course):
        super().__init__(name, gender, age)
        self.roll_no = roll_no
        self.course = course

    def display(self):
        super().display()
        print(f"Roll no: {self.roll_no}   Course: {self.course}")

student_instance1 = Student("Ashik", "male", 21, 234, "python")
student_instance1.display()
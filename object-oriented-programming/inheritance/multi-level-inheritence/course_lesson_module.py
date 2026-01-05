class Course:
    course_name : str

    def __init__(self, course_name):
        self.course_name = course_name

    def display(self):
        print(f"Course name : {self.course_name}")


class Module(Course):
    module_name : str

    def __init__(self, course_name, module_name):
        super().__init__(course_name)
        self.module_name = module_name

    def display(self):
        super().display()
        print(f"Module name : {self.module_name}")


class Lesson(Module):
    lesson_name : str

    def __init__(self, course_name, module_name, lesson_name):
        super().__init__(course_name, module_name)
        self.lesson_name = lesson_name

    def display(self):
        super().display()
        print(f"Lesson name : {self.lesson_name}")


lesson_instance1 = Lesson("Python", "Object Oriented Programming", "Inheritence")
lesson_instance1.display()
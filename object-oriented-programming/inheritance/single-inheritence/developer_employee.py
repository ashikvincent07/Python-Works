class Employee:
    id : str
    department : str
    salary : int

    def __init__(self, id, dept, salary):
        self.id = id
        self.department = dept
        self.salary = salary

    def display(self):
        print(f"ID: {self.id}  Department: {self.department}  Salary: {self.salary}")


class Developer(Employee):
    programming_language : str
    framework : str

    def __init__(self, id, dept, salary, lang, framework):
        super().__init__(id, dept, salary)
        self.programming_language = lang
        self.framework = framework

    def display(self):
        super().display()
        print(f"Programming Language: {self.programming_language}  Framework: {self.framework}")


developer_instance1 = Developer("asd321","frontend",35000,"javascript","angular")
developer_instance1.display()
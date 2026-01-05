class Framework:

    name:str
    language:str
    architecture:str

    def set_framework(self, name, lang, archit):
        self.name = name
        self.language = lang
        self.architecture = archit

    def display(self):
        print(f"Framework name : {self.name}",end=", ")
        print(f"Language : {self.language}",end=", ")
        print(f"architecture : {self.architecture}")

django = Framework()
asp = Framework()
angular = Framework()

django.set_framework("Django","Python","mvc")
angular.set_framework("Angular","Typescript","component")
asp.set_framework("ASP","c#","mvc")

django.display()
angular.display()
asp.display()
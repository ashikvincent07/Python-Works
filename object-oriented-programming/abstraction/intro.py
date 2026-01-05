from abc import ABC
from abc import abstractmethod


class Editor(ABC):

    @abstractmethod
    def create_module_and_package(self):
        pass

    @abstractmethod
    def edit(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def debug(self):
        pass

class VScode(Editor):

    def create_module_and_package(self):
        print("VS code create module and package")

    def edit(self):
        print("vs code edit")

    def execute(self):
        print("vs code execute")

    def debug(self):
        print("vs code debug")

    
vs_code_instance = VScode()

from abc import ABC
from abc import abstractmethod

class Laptop:

    @abstractmethod
    def charge(self):
        pass

    @abstractmethod
    def power_on(self):
        pass

    @abstractmethod
    def power_off(self):
        pass

class HpVictus(Laptop):

    def charge(self):
        print("Hp victus charging")

    def power_on(self):
        print("Hp victus power ON")

    def power_off(self):
        print("Hp victus power OFF")

hp_victus_instance = HpVictus()


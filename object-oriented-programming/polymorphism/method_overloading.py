"""
Docstring for object-oriented-programming.polymorphism.intro

Method overloading(not supported in python)

same method name with different number of parameters in a class.
(python only executes the last initialiazed method.)
"""


class Calculator:
    def mult(self, n1, n2, n3):
        print(n1 * n2 * n3)

    def mult(self, n1, n2):
        print(n1 * n2)

calc_instance = Calculator()

calc_instance.mult(1, 7, 5)
calc_instance.mult(1, 2)
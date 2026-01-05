class Calculator:

    def add(self, *args):
        print(sum(args))

    def mult(self, *args):
        product = 1
        for n in args:
            product *= n
        print(product)


calc_instance1 = Calculator()

calc_instance1.add(12, 34, 4)
calc_instance1.add(11, 34, 11, 19)

calc_instance1.mult(4, 5, 3)
class Fibbonacci:

    def solution(self, limit):
        prev = 0
        current = 1
        for _ in range(limit):
            print(prev)
            prev, current = current, prev + current
             
fib_instance = Fibbonacci()

fib_instance.solution(10)


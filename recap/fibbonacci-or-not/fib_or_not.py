class FibbonacciNumber:

    def solution(self, number):

        is_fibb_number = False

        prev = 0
        current = 1

        while current <= number:
            if current == number:
                is_fibb_number = True
                break
            prev, current = current, prev + current

        return is_fibb_number
    
fibb_instance = FibbonacciNumber()
print(fibb_instance.solution(13))
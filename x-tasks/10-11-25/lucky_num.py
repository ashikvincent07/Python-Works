import random

def lucky_number():

    num_range = range(1, 101)

    lucky_numb = random.choice(num_range)

    print(f"Your lucky number is: {lucky_numb}")


lucky_number()
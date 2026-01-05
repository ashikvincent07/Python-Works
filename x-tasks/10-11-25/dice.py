import random

def roller_dice():

    dice_range = (1, 2, 3, 4, 5, 6)

    choice = random.choice(dice_range)

    print(choice)

roller_dice()
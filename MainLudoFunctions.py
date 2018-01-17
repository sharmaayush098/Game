import random


def start():
    n = input(print("Enter the number of n want to play the game"))
    try:
        if 2 <= int(n) <= 4:
            print(" %s players will start the play" % n)
        else:
            print("Wrong input,that not less than 2 and not more than 4")
    except ValueError:
        print("Please input numeric value")


def path():
    a =list(range(0, 57))
    return a


def dice_numbers():
    return list(range(1, 7))


def random_number():
    return random.randrange(1, 7)


def coins():
    coin_1 = 0
    coin_2 = 0
    coin_3 = 0
    coin_4 = 0

    for number in dice_numbers():
        coin_1 += number
        coin_2 += number
        coin_3 += number
        coin_4 += number


def safe_positions():
    return [0, 8, 13, 21, 26, 34, 39, 47]




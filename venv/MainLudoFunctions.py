import random
def start():
    players = input(print("Enter the number of players want to play the game"))
    try:
        if 2 <= int(players) <=4:
            print(" %s Players will start the play" % n)
        else:
            print("Wrong input,that not less than 2 and not more than 4")
    except ValueError:
        print("Please input numeric value")


def path():
    list(range(0,57))


def dice_number():
    return list(range(1,7))


def random_number():
    return random.choice(list(range(1,7)))


def coins():
    coin_1 = 0
    coin_2 = 0
    coin_3 = 0
    coin_4 = 0
    for number in dice_number():
        coin_1 += number
        coin_2 += number
        coin_3 += number
        coin_4 += number


def safe_positions():
    return [0,8,13,21,26,34,39,47]




from MainLudoFunctions import path
from MainLudoFunctions import safe_positions
from MainLudoFunctions import random_number
Players = ["player1", "player2", "player3", "player4"]
initial_positions = {
            "player_1": {"coin_1": {"current_position": path()[0],
                                    "final_destination": path()[-1],
                                    "safe_positions": safe_positions()},
                         "coin_2": {"current_position": path()[0],
                                    "final_destination": path()[-1],
                                    "safe_positions": safe_positions()},
                         "coin_3": {"current_position": path()[0],
                                    "final_destination": path()[-1],
                                    "safe_positions": safe_positions()},
                         "coin_4": {"current_position": path()[0],
                                    "final_destination": path()[-1],
                                    "safe_positions": safe_positions()}
                         },
            "player_2": {"coin_1": {"current_position": path()[26],
                                    "final_destination": path()[-1],
                                    "safe_positions": safe_positions()},
                         "coin_2": {"current_position": path()[26],
                                    "final_destination": path()[-1],
                                    "safe_positions": safe_positions()},
                         "coin_3": {"current_position": path()[26],
                                    "final_destination": path()[-1],
                                    "safe_positions": safe_positions()},
                         "coin_4": {"current_position": path()[26],
                                    "final_destination": path()[-1],
                                    "safe_positions": safe_positions()}
                         },
            "player_3": {"coin_1": {"current_position": path()[13],
                                    "final_destination": path()[-1],
                                    "safe_positions": safe_positions()},
                         "coin_2": {"current_position": path()[13],
                                    "final_destination": path()[-1],
                                    "safe_positions": safe_positions()},
                         "coin_3": {"current_position": path()[13],
                                    "final_destination": path()[-1],
                                    "safe_positions": safe_positions()},
                         "coin_4": {"current_position": path()[13],
                                    "final_destination": path()[-1],
                                    "safe_positions": safe_positions()}
                         },
            "player_4": {"coin_1": {"current_position": path()[39],
                                    "final_destination": path()[-1],
                                    "safe_positions": safe_positions()},
                         "coin_2": {"current_position": path()[39],
                                    "final_destination": path()[-1],
                                    "safe_positions": safe_positions()},
                         "coin_3": {"current_position": path()[39],
                                    "final_destination": path()[-1],
                                    "safe_positions": safe_positions()},
                         "coin_4": {"current_position": path()[39],
                                    "final_destination": path()[-1],
                                    "safe_positions": safe_positions()}
                         }


            }
"""current positions of all coins for player 1"""
coin1_position = initial_positions["player_1"]["coin_1"]["current_position"]
coin2_position = initial_positions["player_1"]["coin_2"]["current_position"]
coin3_position = initial_positions["player_1"]["coin_3"]["current_position"]
coin4_position = initial_positions["player_1"]["coin_4"]["current_position"]

"""final destination for all coins for player 1"""
coin1_destination = initial_positions["player_1"]["coin_1"]["final_destination"]
coin2_destination = initial_positions["player_1"]["coin_2"]["final_destination"]
coin3_destination = initial_positions["player_1"]["coin_3"]["final_destination"]
coin4_destination = initial_positions["player_1"]["coin_4"]["final_destination"]

"""current positions of all coins for player 2"""
p2coin1_position = initial_positions["player_2"]["coin_1"]["current_position"]
p2coin2_position = initial_positions["player_2"]["coin_2"]["current_position"]
p2coin3_position = initial_positions["player_2"]["coin_3"]["current_position"]
p2coin4_position = initial_positions["player_2"]["coin_4"]["current_position"]

"""final destination for all coins for player 2"""
p2coin1_destination = initial_positions["player_2"]["coin_1"]["final_destination"]
p2coin2_destination = initial_positions["player_2"]["coin_2"]["final_destination"]
p2coin3_destination = initial_positions["player_2"]["coin_3"]["final_destination"]
p2coin4_destination = initial_positions["player_2"]["coin_4"]["final_destination"]

print("*" * 20 + "LUDO GAME" + "*"*20)
print(" ")
print("""Instructions: Ludo Game requires minimum 2 players and maximum 4 players
              to play the game.""")
print("*"*49)
players_count = input("How many players want to play?")
try:
    if int(players_count) == 2:
        print(Players[0] + "And" + Players[1] + " will start the game.")
        while True:
            input(Players[0] + "Turn>>>")
            number_player1 = random_number()
            print(number_player1)
            while number_player1 == 6:
                print("Coin_1 comes In ~  position %s and final point %s" % (coin1_position, coin1_destination))
                input(Players[0])
                print(random_number())
                break
            input(Players[1] + "Turn>>>")
            number_player2 = random_number()
            print(number_player2)
            while number_player2 == 6:
                print("Coin_1 comes In ~  position %s and final point %s" % (p2coin1_position, p2coin1_destination))
                input(Players[1])
                print(random_number())
                break
            continue

    elif int(players_count) == 3:
        print(Players[0] + "," + Players[1] + "," + Players[2] + " will start the game.")

    elif int(players_count) == 4:
        print(Players[0] + "," + Players[1] + "," + Players[2] + "," + Players[3] + " will start the game.")

    else:
        print("Wrong Input,please read the instructions")
except ValueError:
    print("Enter numeric value")


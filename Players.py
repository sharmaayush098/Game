from MainLudoFunctions import path
from MainLudoFunctions import safe_positions


def players():
    players_count = input(print("Enter the number of players want to play: "))
    if players_count == 2:
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
                         }
        }
    elif players_count == 3:
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
                         }
        }

    else:
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








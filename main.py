from random import choice


class Ludo(object):

    def __init__(self, player_count=2):
        self.player_count = player_count
        if player_count == 2:
            self.initial_position = {
                "player1": {"coin1": {"current_position": 0, "moves_left": 56, "is_movable": False},
                            "coin2": {"current_position": 0, "moves_left": 56, "is_movable": False},
                            "coin3": {"current_position": 0, "moves_left": 56, "is_movable": False},
                            "coin4": {"current_position": 0, "moves_left": 56, "is_movable": False}},
                "player2": {"coin1": {"current_position": 0, "moves_left": 56, "is_movable": False},
                            "coin2": {"current_position": 0, "moves_left": 56, "is_movable": False},
                            "coin3": {"current_position": 0, "moves_left": 56, "is_movable": False},
                            "coin4": {"current_position": 0, "moves_left": 56, "is_movable": False}}
            }

        else:
            self.initial_position = {
                "player1": {"coin1": {"current_position": 0, "moves_left": 56, "is_movable": False},
                            "coin2": {"current_position": 0, "moves_left": 56, "is_movable": False},
                            "coin3": {"current_position": 0, "moves_left": 56, "is_movable": False},
                            "coin4": {"current_position": 0, "moves_left": 56, "is_movable": False}},
                "player2": {"coin1": {"current_position": 0, "moves_left": 56, "is_movable": False},
                            "coin2": {"current_position": 0, "moves_left": 56, "is_movable": False},
                            "coin3": {"current_position": 0, "moves_left": 56, "is_movable": False},
                            "coin4": {"current_position": 0, "moves_left": 56, "is_movable": False}},
                "player3": {"coin1": {"current_position": 0, "moves_left": 56, "is_movable": False},
                            "coin2": {"current_position": 0, "moves_left": 56, "is_movable": False},
                            "coin3": {"current_position": 0, "moves_left": 56, "is_movable": False},
                            "coin4": {"current_position": 0, "moves_left": 56, "is_movable": False}},
                "player4": {"coin1": {"current_position": 0, "moves_left": 56, "is_movable": False},
                            "coin2": {"current_position": 0, "moves_left": 56, "is_movable": False},
                            "coin3": {"current_position": 0, "moves_left": 56, "is_movable": False},
                            "coin4": {"current_position": 0, "moves_left": 56, "is_movable": False}}
            }

    def roll_dice(self):
        return choice([1, 2, 3, 4, 5, 6])


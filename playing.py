from main import Ludo


class Player(Ludo):

    def __init__(self):
        super().__init__()

    def user_location(self, player_count, player, coin):
        if player_count==2:
            return self.initial_position[player][coin]["current_position"]
        elif player_count==4:
            return self.initial_position[player][coin]["current_position"]
        else:
            return None

    def moves(self, player, coin, count):
        self.initial_position[player][coin]["current_position"] += count
        self.initial_position[player][coin]["moves_left"] -= count
        if count == 6:
            return True
        else:
            return False

    def coins_status(self, player, coin):
        return self.initial_position[player][coin]["is_movable"]

    def all_coin_status(self, player, ):


class StartGame(Ludo):

    def __init__(self, players):
        super().__init__(players)


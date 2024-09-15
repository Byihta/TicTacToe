from enum import Enum

class GameState(Enum):
    ONGOING = 0
    PLAYER_ONE_WINS = 1
    PLAYER_TWO_WINS = 2
    DRAW = 3

    
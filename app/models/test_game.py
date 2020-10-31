import unittest
from models.player_class import Player
from models.game_class import Game
from models.game_function import * 
# ^^is this * going import too much and break it?#

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player("James", "Rock")
        self.player_2 = Player("Angela", "Scissors")

    #how do i test outcomes?
    # def test_outcomes(self):
    #     append event
    #     assert equals?




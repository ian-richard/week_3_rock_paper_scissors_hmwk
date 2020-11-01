import unittest
from models.player_class import Player
from models.game_class import Game
from models.game_function import * 

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player("James", "Rock")
        self.player_2 = Player("Angela", "Scissors")

        self.round_1 = Game()

    def test_winner_calculation(self):
        self.

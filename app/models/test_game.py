import unittest
from models.player_class import Player
from models.game_class import Game
# from models.game_function import * 
# ^^is this * going import too much and break it?#

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player("James", "Rock")
        self.player_2 = Player("Angela", "Scissors")
        self.round_1 = Game(self.player_1, self.player_2)

    def test_winner(self):
        self.round_1.add_new_winner(self.player_1)
        self.assertEqual(1, len(self.round_1.winner))

    def test_who_has_won(self):
        result = self.round_1.who_has_won(self.player_1, self.player_2)
        self.assertEqual("player 1 wins", result)
    

    







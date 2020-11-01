import unittest
from models.player_class import Player
from models.game_class import Game
# from models.game_function import * 
# ^^is this * going import too much and break it?#

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player("James", "Rock")
        self.player_2 = Player("Angela", "Scissors")
    
        self.outcome1wins = Game("Player 1 wins")
        self.outcome2wins = Game("player 2 wins")
        self.outcome3draw = Game("Draw!")

        self.outcomes = [self.outcome1wins, self.outcome2wins, self.outcome3draw]

    # def test_outcome(self):
    #     # self.game.add_new_outcome(self.outcome1wins)
    #     self.assertEqual(1, len(self.outcome1wins.outcome))
    
    def test_game_has_outcome(self):
        self.assertEqual("Player 1 wins", self.outcome1wins.outcome)







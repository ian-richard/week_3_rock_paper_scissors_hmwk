import unittest
from models.player_class import Player
from models.game_class import Game
# from models.game_function import * 
# ^^is this * going import too much and break it?#

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player("Rock")
        self.player_2 = Player("Scissors")
        self.player_3 = Player("Paper")
        self.player_4 = Player("Rock")
        self.round_1 = Game(self.player_1, self.player_2)
        self.round_2 = Game(self.player_1, self.player_3)
        self.round_3 = Game(self.player_1, self.player_4)

    def test_winner(self):
        self.round_1.add_new_winner(self.player_1)
        self.assertEqual(1, len(self.round_1.winner))

    def test_who_has_won_text_return(self):
        result = self.round_1.who_has_won_text_return(self.player_1, self.player_2)
        self.assertEqual("player 1 wins", result)
    
    def test_winner_list__player_1_wins(self):
        result = self.round_1.winner_in_list(self.player_1, self.player_2)
        self.assertEqual(1, len(self.round_1.winner))
    
    def test_winner_list__player_3_wins(self):
        result = self.round_2.winner_in_list(self.player_1, self.player_3)
        self.assertEqual(1, len(self.round_2.winner))
    
    def test_winner_list__draw(self):
        result = self.round_3.winner_in_list(self.player_1, self.player_4)
        self.assertEqual(0, len(self.round_3.winner))
    

    







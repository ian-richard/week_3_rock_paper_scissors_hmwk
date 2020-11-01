import unittest
from models.player_class import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("Rock")

    # def test_player_has_name(self):
    #     self.assertEqual("John", self.player.player_name)
    
    def test_player_has_choice(self):
        self.assertEqual("Rock", self.player.choice)


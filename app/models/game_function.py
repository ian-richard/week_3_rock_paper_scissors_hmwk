from models.game_class import *
from models.player_class import *

outcome1wins = Game("player 1 wins")
outcome2wins = Game("player 2 wins")
outcome3draw = Game("Draw!")

outcomes = [outcome1wins, outcome2wins, outcome3draw]

    def add_new_outcome(outcome):
        outcomes.append(outcome)

    def number_of_outcomes(self):
        return len(self.outcome)
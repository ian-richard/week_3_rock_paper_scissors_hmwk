class Game:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.winner = []


    def add_new_winner(self, player):
        self.winner.append(player)

    def who_has_won(self, player_1, player_2):
        if player_1.choice == "Rock" and player_2.choice == "Scissors":
            return "player 1 wins"
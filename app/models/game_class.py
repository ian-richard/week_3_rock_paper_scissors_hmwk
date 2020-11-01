class Game:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.winner = []


    def add_new_winner(self, player):
        self.winner.append(player)
    
    def winner_in_list(self, player_1, player_2):
        if player_1.choice == "Rock" and player_2.choice == "Scissors":
            self.winner.append(player_1)
            return player_1
        elif player_1.choice == "Scissors" and player_2.choice == "Paper":
            self.winner.append(player_1)
            return player_1
        elif player_1.choice == "Paper" and player_2.choice == "Rock":
            self.winner.append(player_1)
            return player_1
        elif player_1.choice == player_2.choice:
            return None
        else:
            self.winner.append(player_2)
            return player_2


    
    def who_has_won_text_return(self, player_1, player_2):
        if player_1.choice == "Rock" and player_2.choice == "Scissors":
            return "player 1 wins"
        
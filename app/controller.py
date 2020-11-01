from flask import render_template, request, redirect
from app import app
from app.models.game_class import *
from app.models.player_class import *

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results', methods=['POST'])
def add_player():
    P1_name = request.form['P1_name']
    P2_name = request.form['P2_name']
    P1_choice = request.form['P1_choice']
    P2_choice = request.form['P2_choice']
    player_1 = Player(player_name=P1_name, choice=P1_choice)
    player_2 = Player(player_name=P2_name, choice=P2_choice)
    my_game = Game(player_1, player_2)
    
    result = my_game.winner_in_list(player_1, player_2)
    
    return render_template('results.html', result=result)
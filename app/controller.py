from flask import render_template, request, redirect
from app import app
from app.models.game_class import *
from app.models.player_class import *

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add-match', methods=['POST'])
def add_player():
    P1_choice = request.form['P1_choice']
    P2_choice = request.form['P2_choice']
    player_1 = Player(choice=P1_choice)
    player_2 = Player(choice=P2_choice)
    winner_in_list(player_1, player_2)
    return redirect('/')
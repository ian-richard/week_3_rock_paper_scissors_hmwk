from flask import render_template, request, redirect
from app import app
# from app.models.game_function import *
from app.models.game_class import *
from app.models.player_class import *

@app.route('/')
def index():
    return render_template('index.html')
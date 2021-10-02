from flask import Flask, render_template, redirect, session, request
from random import choice, randint
from boggle import Boggle
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = 'chickenz'

boggle_game = Boggle()
BOARD_KEY = 'HA12'
HIGHEST_SCORE_KEY='HS13'
GAMES_PLAYED_KEY='GP14'
boardDict = {}

@app.route('/base')
def base():
    # board = boggle_game.make_board()
    return render_template('base.html', board=board, boggle=boggle_game)    

@app.route('/')
def start():
    return render_template('start.html')

@app.route('/display')
def play():
    """directs user to board page after customizing board from start page"""
    size=int(request.args['size'])
    time=int(request.args['time'])
    session[BOARD_KEY] = boggle_game.make_board(int(size))
    board=session[BOARD_KEY]
    gamesPlayed=session[GAMES_PLAYED_KEY]
    highScore=int(session[HIGHEST_SCORE_KEY])
    return render_template('base.html', time=time, size=size, board=board, boggle=boggle_game, gamesPlayed=gamesPlayed, highScore=highScore)

@app.route('/guess/<word>')
def guess(word):
    """When was word is passed, will check to see if the word is valid for the current board created. 
    
    Returns ok, not-word, and not-on-board
    
    ex. /guess/cat
    
    Tests are difficult to run since the board is randomly created."""


    board = session[BOARD_KEY]
    return boggle_game.check_valid_word(board, word)

@app.route('/post/<score>', methods=['POST'])
def postResults(score):
    gamesPlayed = session[GAMES_PLAYED_KEY]
    if gamesPlayed == 0:
        session[HIGHEST_SCORE_KEY] = score
    else:
        highScore = session[HIGHEST_SCORE_KEY]
        if score > highScore:
            session[HIGHEST_SCORE_KEY] = score
    session[GAMES_PLAYED_KEY] = gamesPlayed + 1
    return redirect('/')
        
    
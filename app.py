from flask import *
from logic import *
import sys
import os

app = Flask(__name__)

# GLOBAL VARIABLES
board = {}
turn = {1: 'v'}
response = 'Do your turn!'
game_mode = None
restart = None


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def menu():

    global board, turn, response, game_mode, restart

    board = {}
    turn[1] = 'v'
    game_mode = None
    response = 'Do your turn!'
    restart = None

    return render_template('menu.jinja2')


@app.route('/game', methods=['GET', 'POST'])
def game():

    global board, turn, response, game_mode, restart

    game_mode = request.form.get('game_mode', game_mode)

    if game_mode is None:
            return redirect('/')

    else:
            if len(board) == 0:
                board = engine.set_start_board(board)

            restart = request.form.get('restart', None)

            if restart is not None:
                board = engine.set_start_board(board)
                turn[1] = 'v'
                response = 'Do your turn!'
                restart = None

            json_input = request.get_json()

            if json_input is not None:
                start_row = json_input.get('start_row')
                start_column = json_input.get('start_column')
                end_row = json_input.get('end_row')
                end_column = json_input.get('end_column')

                if game_mode == 'hotseat' or game_mode == 'multiplayer':
                    response = engine.check_legal_moves(start_row, start_column, end_row, end_column, board, turn)

                if game_mode == 'singleplayer' and turn[1] == 'v':
                    response = engine.check_legal_moves(start_row, start_column, end_row, end_column, board, turn)

            if game_mode == 'singleplayer' and turn[1] == 'b':
                engine.ai(board, turn)

            return render_template('game.jinja2', game_mode=game_mode, board=board, response=response, turn=turn)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
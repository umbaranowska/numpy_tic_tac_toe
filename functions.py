import numpy as np

def generate_board():

    board = np.array([['.','.','.'],
                     ['.','.','.'],
                     ['.','.','.']])

    return board

def ask_who_begins_game():

    who_begins_game = input('who begins the game? [x/o] ')

    while who_begins_game not in ['x', 'o']:
        print('player must be x or o, try again')
        who_begins_game = input('who begins the game? [x/o] ')

    return who_begins_game

def get_coordinates_from_player(current_player):

    print(f'your move {current_player}!')

    row = int(input('which row? [0/1/2] '))
    while row not in [0, 1, 2]:
        print('row must be 0-2, try again')
        row = int(input('which row? [0/1/2] '))
    column = int(input('which column? [0/1/2] '))
    while column not in [0, 1, 2]:
        print('column must be 0-2, try again')
        column = int(input('which column? [0/1/2] '))

    coordinates = (row, column)
    return coordinates

def check_coordinates(board, coordinates):

    if board[coordinates] not in ['x', 'o']:
        return True
    else:
        print('there is already a mark here, try again!')
        return False

def put_item_on_board(board, current_player, coordinates):

    board[coordinates] = current_player
    return board

def update_current_player(current_player):

    if current_player == 'x':
        return 'o'
    else:
        return 'x'

def is_game_over(board):

    winning = [['x', 'x', 'x'], ['o', 'o', 'o']]
    to_check = [board[0].tolist(), board[1].tolist(), board[2].tolist(),
                board[:, 0].tolist(), board[:, 1].tolist(), board[:, 2].tolist(),
                board.diagonal().tolist(), np.fliplr(board).diagonal().tolist()]

    if np.any([x in winning for x in to_check]):
        return True
    elif np.any(board == '.') == False:
        return True
    else:
        return False

def check_who_won(board):

    to_check = [board[0].tolist(), board[1].tolist(), board[2].tolist(),
                board[:, 0].tolist(), board[:, 1].tolist(), board[:, 2].tolist(),
                board.diagonal().tolist(), np.fliplr(board).diagonal().tolist()]

    if np.any([x == ['x', 'x', 'x'] for x in to_check]):
        return 'congratulations x won!'
    elif np.any([x == ['o', 'o', 'o'] for x in to_check]):
        return 'congratulations o won!'
    else:
        return 'GAME OVER you both lost!'
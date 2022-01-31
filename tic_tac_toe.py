import numpy as np
from functions import *

current_player = ask_who_begins_game()
board = generate_board()

while is_game_over(board) == False:
    coordinates = get_coordinates_from_player(current_player)
    while check_coordinates(board, coordinates) == False:
        coordinates = get_coordinates_from_player(current_player)
    put_item_on_board(board, current_player, coordinates)
    current_player = update_current_player(current_player)
    print(board)

winner = check_who_won(board)
print(winner)
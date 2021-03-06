# coding: utf-8
""" Functions for drawing simple command-line graphics for Ludo"""
from board import Board # Why do we import board?

# String for displaying the board
empty_board_str = """            ┌──┬──┬──┐            
            │  │  │  │            
            ├──┼──┼──┤            
            │  │  │  │            
            ├──┼──┼──┤            
            │  │  │  │            
            ├──┼──┼──┤            
            │  │  │  │            
┌──┬──┬──┬──┼──┼──┼──┼──┬──┬──┬──┐
│  │  │  │  │  │  │  │  │  │  │  │
├──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┤
│  │  │  │  │  │**│  │  │  │  │  │
├──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┤
│  │  │  │  │  │  │  │  │  │  │  │
└──┴──┴──┴──┼──┼──┼──┼──┴──┴──┴──┘
            │  │  │  │            
            ├──┼──┼──┤            
            │  │  │  │            
            ├──┼──┼──┤            
            │  │  │  │            
            ├──┼──┼──┤            
            │  │  │  │            
            └──┴──┴──┘	            
"""

board_str_width = 35

# Board indexes mapped to positions on the board string
piece_pos_map = [
    (14, 21), (14, 19), (14, 17), (14, 15), (14, 13), (11, 13), (8, 13), (5, 13), (2, 13), (2, 11),
    (2, 9), (5, 9), (8, 9), (11, 9), (14, 9), (14, 7), (14, 5), (14, 3), (14, 1), (17, 1),
    (20, 1), (20, 3), (20, 5), (20, 7), (20, 9), (23, 9), (26, 9), (29, 9), (32, 9), (32, 11),
    (32, 13), (29, 13), (26, 13), (23, 13), (20, 13), (20, 15), (20, 17), (20, 19), (20, 21), (17, 21)
]

exit_pos_map = [
    [(17, 19), (17, 17), (17, 15), (17, 13)],
    [(5, 11), (8, 11), (11, 11), (14, 11)],
    [(17, 3), (17, 5), (17, 7), (17, 9)],
    [(29, 11), (26, 11), (23, 11), (20, 11)]
]

start_pos_map = [(4, 17), (4, 3), (26, 3), (26,17)]

def set_board_value(board_list : list, pos : tuple, value : str):
    """ Set pos at the board string to string value """
    board_list[pos[1]*board_str_width + pos[0]] = value

def display_board(current_board : Board):
    """ Generate a board string which is visualised with print.
    
    Uses the premade empty board string and fills it in with pieces from the Board class
    """
    board_str = list(empty_board_str)

    i = 0
    for piece in current_board.board_state: #Board Main state visualisation
        if piece[0] == 0:
            i += 1
            continue
        if (piece[0] > 1): #This position has more than 1 piece
            pos = piece_pos_map[i]
            set_board_value(board_str, pos, str(piece[1]))
            pos2 = (pos[0] - 1, pos[1])
            set_board_value(board_str, pos2, str(piece[0]))
        else:
            set_board_value(board_str, piece_pos_map[i], str(piece[1]))
        i += 1

    j = 0
    for exit_state in current_board.exit_states: #Board Exit state visualisation
        i = 0
        for piece in exit_state:
            if piece[1] != 0:
                if piece[0] > 1: #More than one piece
                    pos = exit_pos_map[j][i]
                    set_board_value(board_str, pos, str(piece[1]))
                    pos2 = (pos[0] - 1, pos[1])
                    set_board_value(board_str, pos2, str(piece[0]))
                else:
                    set_board_value(board_str, exit_pos_map[j][i], str(piece[1]))
            i += 1
        j += 1

    #Draw starting area
    player = 0
    for count in current_board.start_counts:
        if count > 3: #4
            x,y = start_pos_map[player]
            set_board_value(board_str, (x+3,y+2), str(player+1))
        if count > 2: #3
            x,y = start_pos_map[player]
            set_board_value(board_str, (x,y+2), str(player+1))
        if count > 1: #2
            x,y = start_pos_map[player]
            set_board_value(board_str, (x+3,y), str(player+1))
        if count > 0: #1
            x,y = start_pos_map[player]
            set_board_value(board_str, (x,y), str(player+1))
        player += 1

    print("".join(board_str))

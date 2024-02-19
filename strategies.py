def just_once_except_six(die_face, board):
    res = die_face == 6
    if not res:
        print('Not a 6? I don\'t go on')
    return die_face == 6

def until_three_pos_covered(die_face, board):
    board_positions = board.positions.values()

    return sum(board_positions) <= 3

def until_four_pos_covered(die_face, board):
    board_positions = board.positions.values()
    return sum(board_positions) <= 4

def stop_after_3_or_5(die_face, board):
    return die_face not in [3,5]

def as_long_as_possible(die_face, board):
    return True

strat_list = [just_once_except_six, until_three_pos_covered, until_four_pos_covered, stop_after_3_or_5, as_long_as_possible]
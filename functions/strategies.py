def just_once_except_six(die_face, board):
    """Only continue to play only if the die shows a 6"""
    return die_face == 6

def until_three_pos_covered(die_face, board):
    """Only continue to play if less than 3 positions of the board are occupied by sticks"""
    board_positions = board.positions.values()
    return sum(board_positions) < 3

def until_four_pos_covered(die_face, board):
    """Only continue to play if less than 4 positions of the board are occupied by sticks"""
    board_positions = board.positions.values()
    return sum(board_positions) < 4

def stop_after_3_or_5(die_face, board):
    """Stop playing if the die shows a 3 or a 5"""
    return die_face not in [3,5]

def as_long_as_possible(die_face, board):
    """Continue to play until required to take a stick"""
    return True

strat_list = [just_once_except_six, until_three_pos_covered, until_four_pos_covered, stop_after_3_or_5, as_long_as_possible]
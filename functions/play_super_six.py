from classes.game import Game


def play_super_six(strat_list, num_sticks):

    game = Game(strat_list, num_sticks)

    while True:
        fin = False
        game.round += 1
        for i,s in enumerate(strat_list):
            game.roll_die(i)

            if game.players[i].finished:
                
                fin = True
                winning_strategy = game.players[i].strategy.__doc__
                break
            elif game.board.finished:
                fin = True
                break

        if fin:
            return {
                'strategies_in_game': [s.__name__ for s in strat_list],
                'winning_strategy': winning_strategy,
                'rounds': game.round,
                'sticks_in_container': game.board.content,
                'sticks_in_game': num_sticks
            }

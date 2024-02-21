"""
Play the game Super Six with a chosen set of strategies for a selectable number of games. 
Have the percentage of the wins for each strategy printed to your console as well as more detailed stats saved to csv.
"""

import pandas as pd

from functions.strategies import strat_list
from functions.play_super_six import play_super_six


games_to_play = 100000
playing_strats = [strat_list[3], strat_list[4]]
#playing_strats = strat_list

# AVAILABLE STRATEGIES
# 0 :  Continue to play only if the die shows a 6
# 1 :  Only continue to play if none of the positions of the board are occupied by sticks
# 2 :  Only continue to play if less than 2 positions of the board are occupied by sticks
# 3 :  Only continue to play if less than 3 positions of the board are occupied by sticks
# 4 :  Only continue to play if less than 4 positions of the board are occupied by sticks
# 5 :  Only continue to play if less than 5 positions of the board are occupied by sticks
# 6 :  Stop playing if the die shows a 3 or a 5
# 7 :  Continue to play until required to take a stick

results = pd.DataFrame([play_super_six(playing_strats, 36) for i in range(games_to_play)])
winning_percentages = results['winning_strategy'].value_counts(normalize=True).mul(100).round(1).astype(str) + '%'

print(f'When the strategies {", ".join([f'"{s.__doc__}"' for s in playing_strats])} meet in Super Six, the distribution of wins after {games_to_play: ,d} games looks approximately like this:')
print(winning_percentages.to_markdown())

results.to_csv('data/results.csv', index=False)
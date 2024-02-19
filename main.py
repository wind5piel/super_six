"""
Play the game Super Six with a chosen set of strategies for a selectable number of games. 
Have the percentage of the wins for each strategy printed to your console as well as more detailed stats saved to csv.
"""

import pandas as pd

from functions.strategies import strat_list
from functions.play_super_six import play_super_six


games_to_play = 10000
playing_strats = [strat_list[3], strat_list[4]]
# AVAILABLE STRATEGIES
# 0 :  Only continue to play only if the die shows a 6
# 1 :  Only continue to play if less than 3 positions of the board are occupied by sticks
# 2 :  Only continue to play if less than 4 positions of the board are occupied by sticks
# 3 :  Stop playing if the die shows a 3 or a 5
# 4 :  Continue to play until required to take a stick

results = pd.DataFrame([play_super_six(playing_strats, 36) for i in range(games_to_play)])

print(f'When the strategies {", ".join([f'"{s.__doc__}"' for s in playing_strats])} meet in Super Six, the distribution of wins after {games_to_play} games looks approximately like this:')
print(results['winning_strategy'].value_counts(normalize=True).to_markdown())

results.to_csv('data/results.csv', index=False)
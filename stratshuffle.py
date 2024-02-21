"""
Play the game Super Six with 2 to 6 Players and shuffle the strategies. 
"""
import pandas as pd
from random import randint

from functions.strategies import strat_list
from functions.play_super_six import play_super_six

games_to_play = 1000000
num_strats = len(strat_list)

results = []

for i in range(2,7):
    for g in range(games_to_play):
        playing_strats = [strat_list[randint(0,num_strats-1)] for _ in range(i)]
        results += [play_super_six(playing_strats, 36)]

#pd.DataFrame(results).to_feather('data/all_strat_sim.feather')
pd.DataFrame(results).to_csv('data/all_strat_sim.csv', index=False)
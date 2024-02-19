import pandas as pd

from functions.strategies import strat_list
from functions.play_super_six import play_super_six

results = pd.DataFrame([play_super_six(strat_list, 60) for i in range(1000)])

results.to_csv('data/results.csv')
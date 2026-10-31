import numpy
import pandas
import matplotlib

from ucimlrepo import fetch_ucirepo   #Dataset source

tic_tac_toe_endgame = fetch_ucirepo(id=101)
df = tic_tac_toe_endgame.data.original

print(df.head())

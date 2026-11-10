import numpy
import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv('Genshin Characters List 7.1 .csv')
'''columns ['character_name', 'gender', 'model_type', 'rarity', 'region', 
            'element','weapon_type', 'constellation_name', 'birthday', 'special_dish',
            'ascension_stat', 'date_released', 'release_version', 'tier_rating', 'primary_role']'''

df.set_index('character_name', inplace=True)
dfPartial = df.drop(['model_type','constellation_name', 'birthday', 'special_dish','ascension_stat', 'date_released', 'tier_rating', 'primary_role'], axis = 1 )







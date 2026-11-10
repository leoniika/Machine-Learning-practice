import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Genshin Characters List 7.1 .csv')
'''columns ['character_name', 'gender', 'model_type', 'rarity', 'region', 
            'element','weapon_type', 'constellation_name', 'birthday', 'special_dish',
            'ascension_stat', 'date_released', 'release_version', 'tier_rating', 'primary_role']'''

def extract_region(value):
    if pd.isna(value):
        return value

    if "(in-game)" in value and "(in lore)" in value:
        return value.split("(in-game)")[1].split("(in lore)")[0].strip()
    return value

df.set_index('character_name', inplace=True)
df["region"] = df["region"].apply(extract_region)
dfPartial = df.drop(['model_type','constellation_name', 'birthday', 'special_dish','ascension_stat', 'date_released', 'primary_role'], axis = 1 )


#یک نمودار رسم کن که تعداد کاراکترهای هر منطقه را نشان دهد.

Regions = ['Mondstadt', 'Liyue', 'Inazuma', 'Sumeru', 'Fontaine', 
           'Natlan', 'Nod-Krai', 'Snezhnaya', "Khaenri'ah", 'Simulanka']

CharacterCount = dfPartial['region'].value_counts()  
#output is a series with index as region and values as count of characters in that region
CharacterCount = CharacterCount.reindex(Regions)
#reindexing to make sure the order of regions is correct

plt.bar(CharacterCount.index, CharacterCount.values, 
        width = 0.5, edgecolor = 'black', 
        color = [ 'lightblue', 'goldenrod', 'violet', 'olive', 'turquoise', 'red', '#BAE66C', 'silver', 'beige', 'orange'])

plt.title('Characters per Region')
plt.xlabel('Regions')
plt.ylabel('Number of Characters')
plt.axis(ymax = 25)
plt.xticks(fontsize=10, rotation=45, ha='right', rotation_mode='anchor')


plt.show()





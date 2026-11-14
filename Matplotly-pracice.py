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


#توزیع کاراکترها بر اساس Element

ElementTypes = dfPartial['element'].value_counts()

plt.pie( ElementTypes.values , labels = ElementTypes.index, autopct='%1.1f%%', 
                colors = ['#BDF3FF', '#FF772E', '#BA7CE6', '#45C7F5', '#3C4CC9', '#BDA015', '#8DFF85'])

plt.title('Characters per Element')


#مقایسه انواع سلاح‌ها

WeaponTypes = dfPartial['weapon_type'].value_counts().sort_values()

plt.barh(WeaponTypes.index, WeaponTypes.values)

plt.title('Characters per Weapon')
plt.xlabel('Character Count')
plt.ylabel('Weapon')


#تعداد کاراکترهای منتشرشده در هر release_version را محاسبه و روند آن را با نمودار خطی

version_counts = df.groupby('release_version').size().sort_index()

plt.plot( version_counts.index, version_counts.values, marker = 'o')

plt.title('Characters per Release Version')
plt.xlabel('Release Version')
plt.ylabel('Character Count')


#Working with subplot

plt.figure(figsize=(16, 5))

region_counts = dfPartial['region'].value_counts()
element_counts = dfPartial['element'].value_counts()
weapon_counts = dfPartial['weapon_type'].value_counts()

plt.subplot(1, 3, 1)
plt.bar(region_counts.index, region_counts.values)
plt.title('Characters per Region')
plt.xticks(rotation=45)

plt.subplot(1, 3, 2)
plt.bar(element_counts.index, element_counts.values)
plt.title('Characters per Element')

plt.subplot(1, 3, 3)
plt.bar(weapon_counts.index, weapon_counts.values)
plt.title('Characters per Weapon')
plt.xticks(rotation=45)


#'Element Distribution per Version'

element_version = pd.crosstab(
    df['release_version'],
    df['element']
)

element_version.plot(kind='line', marker='o')

plt.title('Element Distribution per Version')
plt.xlabel('Release Version')
plt.ylabel('Character Count')

plt.legend(title='Element')
plt.grid()

plt.show()





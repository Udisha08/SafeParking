import numpy as np
import pandas as pd


'''
Ranking Stratergy

Factors considered: Crime, openSpaces

1 -> <25 CR and >800 OS
2 -> >25 CR <50 and >600
3 -> >50 CR <75 and >400
4 -> >75 CR <100 and >200
5 -> >100 and <200

'''


def normalizeProbability(x):
    return x/10000


df = pd.read_csv('./data/DataWODays.csv')

df['probability'] = df['probability'].apply(normalizeProbability)
print(min(df['Crime']), min(df['openSpaces']))
print(df['Crime'].mean(), df['openSpaces'].mean())
print(max(df['Crime']), max(df['openSpaces']))


ranks = []
for i in df['Crime']:
    # print(i)
    if i <= 25:
        ranks.append(1)
    elif 25 < i <= 50:
        ranks.append(2)
    elif 50 < i <= 75:
        ranks.append(3)
    elif 75 < i <= 100:
        ranks.append(4)
    else:
        ranks.append(5)

df['ranks'] = ranks
print(df)
if 37.74295 in df.Latitude and -122.42648 in df.Longitude:
    print("True")
print(df['ranks'].unique())

df.to_csv('./data/dataWithRanks.csv')

import pandas as pd
import numpy as np

df = pd.read_csv('https://analityk.edu.pl/wp-content/uploads/2020/12/film.csv',
                 encoding='ISO-8859-1',
                 skiprows=[1],
                 sep=';',
                 usecols=['Year', 'Length', 'Title', 'Subject', 'Popularity', 'Awards'],
                 dtype={'Length': 'float64', 'Popularity': 'float64'},
                 converters={'Awards': lambda x: True if x == 'Yes' else False})
print(df.head().to_string())
print(df.groupby('Year').count())
print(df.groupby('Year').Popularity.mean())
print(df.groupby(['Year','Subject']).Length.mean())

print('..................')

# grupuj po roku, wyświetl kilka rzeczy, o które poproszę
print(df.groupby('Year').agg({'Popularity': ['min', 'max'], 'Length': ['min', 'max']}))

#to samo, ale nadaj nazwy kolumnom
print(df.groupby('Year').agg(minimalna_popularnosc=('Popularity','min'),
                             maksymalna_popularnosc=('Popularity', 'max')))

#sortowanie
print(df[(df['Year'] >= 1982) & (df['Year'] <= 1990)])
print(df[(df['Year'] >= 1982) & (df['Year'] <= 1990)].groupby('Year').Length.mean())

print(df)
#dodanie kolumny
df['new'] = df['Year'] - 5
df['newer'] = np.random.random(1659)

#usuwanie kolumn
df.drop('new', axis=1, inplace=True)

#dodać wiersz
df.loc[3,:] = [199999, 3232, 'title', 5, 6, 7, 5]

#usun wiersz
df.drop(3, axis=0, inplace=True)

#dodać kolumne w danej pozycji
df.insert(2, 'new', np.random.random())



print(df)

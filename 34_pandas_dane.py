import pandas as pd

df = pd.read_csv('https://analityk.edu.pl/wp-content/uploads/2020/12/film.csv',
                 encoding='ISO-8859-1',
                 skiprows=[1],
                 sep=';',
                 usecols=['Year', 'Length', 'Title', 'Subject', 'Popularity', 'Awards'],)


print(df.head().to_string())
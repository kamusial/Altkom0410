import pandas as pd

path = 'C:\\Users\\musiakam\\Desktop\\Firma\\6. Altkom\\4. Python analiza danych\\Altkom0410\\pliki\\pokemon.csv'
df = pd.read_csv(path, delimiter=',')

print(df.head(4).to_string())

print(df[['Name', 'Type 1', 'HP']][0:5])
print(df.iloc[1:4])  #zakres wierszy, wsyzstkie kolumny
print(df.iloc[2,1])   #konkretne pole

print(df.loc[df['Type 1'] == 'Fire'])

print(df.describe().T.to_string())

print(df.sort_values('Name', ascending=False))
print(df.sort_values(['Type 1','Speed'], ascending=[1, 0]))

df['Total'] = df['HP'] + df['Attack'] + df['Defense']
print(df.head())
del df['Type 1']

df.to_csv('C:\\Users\\musiakam\\Desktop\\Firma\\6. Altkom\\4. Python analiza danych\\Altkom0410\\pliki\\NEW_pokemon.csv',
          index=False, sep=';')

df.to_excel('C:\\Users\\musiakam\\Desktop\\Firma\\6. Altkom\\4. Python analiza danych\\Altkom0410\\pliki\\NEW_pokemon.xlsx',
          index=False)

df.to_csv('C:\\Users\\musiakam\\Desktop\\Firma\\6. Altkom\\4. Python analiza danych\\Altkom0410\\pliki\\NEW_pokemon.txt',
          index=False, sep='\t')


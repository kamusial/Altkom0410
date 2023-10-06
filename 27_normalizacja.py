import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('C:\\Users\\musiakam\\Desktop\\Firma\\6. Altkom\\4. Python analiza danych\\Altkom0410\\pliki\\auta.csv',
                 encoding='ISO-8859-1')
print(df)
scale = StandardScaler()

#df['Tom2'] = df.Tom.str[:1] + '.' + df.Tom.str[2:]
df['Tom'] = df.Tom.str.replace(',','.')
print(df)

X = df[['Tom', 'Waga']]

scaledX = scale.fit_transform(X)
scaledX = pd.DataFrame(scaledX)
print(type(X))
print(type(scaledX))

print(X)
print(scaledX)



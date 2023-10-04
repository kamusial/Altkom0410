import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('otodom.csv')
print(df)

print(df.describe().T.to_string())   #T - zamiana wierszy, z kolumnami

print('Korelacja')

#print(df.iloc[2,0])   #wiersz, kolumna
print(df.iloc[:,1:])   #bez pierwszej kolumny

print(df.iloc[:,1:].corr())

#plt.imshow(df.iloc[:,1:].corr())
# sns.heatmap(df.iloc[:,1:].corr(), annot=True)
# plt.show()

q1 = df.describe().loc['25%','cena']
q3 = df.describe().loc['75%','cena']

df1 = df[(df.cena >= q1) & (df.cena <= q3) & (df.rok_budowy < df.describe().loc['max','rok_budowy'])]

# plt.hist(df1.cena)
# plt.show()
# sns.histplot(df1.cena)
# plt.show()

print('teraz dane')
print(df.columns)

X = df1.iloc[:,2:]   #liczba_pieter  liczba_pokoi  pietro  powierzchnia  rok_budowy
y = df1.cena

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#wybór i trenowanie modelu
model = LinearRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(model.coef_)

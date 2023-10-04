import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

df = pd.read_csv('diabetes.csv')
print(df.describe().T.to_string())
print('\n\n\npuste wyniki')
print(df.isna().sum())

for col in ['glucose', 'bloodpressure', 'skinthickness', 'insulin',
       'bmi', 'diabetespedigreefunction', 'age']:
    df[col].replace(0, np.NaN, inplace=True)   #zamiana zer na NaN
    mean_ = df[col].mean()
    df[col].replace(np.NaN, mean_, inplace=True)
print(df.isna().sum())
print(df.describe().to_string())

df.to_csv('cukrzyca_dobre_dane.csv')

df.to_csv('cukrzyca.csv')   #
X = df.iloc[:, :-1]
y = df.outcome

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('iris.csv')
print(df.head())
print(df['class'].value_counts())

species = {
    "Iris-setosa":0, "Iris-versicolor":1, "Iris-virginica":2
}

df['class_value'] = df['class'].map(species)
print(df.head())

# sns.scatterplot(data=df, x='sepallength', y='sepalwidth', hue='class')
# plt.title('Sepal')
# plt.show()
# sns.scatterplot(data=df, x='petallength', y='petalwidth', hue='class')
# plt.title('Petal')
# plt.show()

print(df.columns)
sns.heatmap(df.iloc[:,:4].corr(), annot=True)
plt.show()
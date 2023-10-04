import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('iris.csv')
print(df.head())
print(df['class'].value_counts())

species = {
    "Iris-setosa":0, "Iris-versicolor":1, "Iris-virginica":2'
}
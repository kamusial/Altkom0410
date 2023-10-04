import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression   # scikit-learn

df = pd.read_csv('weight-height.csv')
print(df)
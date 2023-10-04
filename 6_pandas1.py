import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression   # scikit-learn

df = pd.read_csv('weight-height.csv')
print(type(df))
print(df.head(8))
print(df.Height)   #dana kolumna
print(df.Gender.value_counts())
df.Height *= 2.54
df.Weight /= 2.2
print(df.head(8))
# plt.hist(df.Weight, 40)
# plt.show()

# plt.hist(df.query("Gender=='Male'").Weight, 40, color='red')
# plt.hist(df.query("Gender=='Female'").Weight, 40)
# plt.show()

# sns.histplot(df.query("Gender=='Male'").Weight)
# sns.histplot(df.query("Gender=='Female'").Weight)
# plt.show()

sns.histplot(df, x=df.Weight, hue='Gender', element='poly')  #bars, step
plt.show()
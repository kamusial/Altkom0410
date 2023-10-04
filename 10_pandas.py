import pandas as pd

df = pd.read_csv('heart.csv', comment='#')
print(df.head(5).to_string())
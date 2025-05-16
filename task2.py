import pandas as pd

df = pd.read_csv('cat_breeds_clean.csv')
x = df[df['Age_in_months'] < 5]
print(x)

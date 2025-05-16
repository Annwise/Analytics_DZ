import pandas as pd

df = pd.read_csv('cat_breeds_clean.csv')
df_sorted = df.sort_values('Weight', ascending=True)
print(df_sorted.head())

import pandas as pd

df = pd.read_csv('cat_breeds_clean.csv')
age_cat = df['Age_in_years'].agg(['mean', 'median', 'max'])
print(age_cat)

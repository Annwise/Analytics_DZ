import pandas as pd

df = pd.read_csv('cat_breeds_clean.csv')
age_gender = df.groupby('Gender')['Age_in_months'].mean()
print(age_gender)

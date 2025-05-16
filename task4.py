import pandas as pd

df = pd.read_csv('cat_breeds_clean.csv')
x = df.nlargest(5, 'Body_length')
print(x)

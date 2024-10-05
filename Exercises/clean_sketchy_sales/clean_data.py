import pandas as pd

df = pd.read_csv("messy_sales_data.csv")
print(df.to_string())

mean = df["Price"].mean()
print(mean)

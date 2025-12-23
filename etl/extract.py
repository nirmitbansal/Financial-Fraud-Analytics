import pandas as pd

print("Reading CSV file...")

df = pd.read_csv("data/raw/creditcard.csv")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print(df.head())

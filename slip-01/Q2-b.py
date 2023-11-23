# B) Write a Python program to view basic statistical details of the data.(Use wineequality-red.csv)
import pandas as pd

df = pd.read_csv("winequality-red.csv")

print("Statistical details")
print(df.describe())

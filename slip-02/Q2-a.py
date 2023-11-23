# Q.2 A) Write a Python program for Handling Missing Value. Replace missing value of salary, 
# age column with mean of that column.(Use Data.csv file)
import pandas as pd

df = pd.read_csv("Data.csv")
print(df)
agemean = df['Age'].mean()
salarymean = df['Salary'].mean()
df['Age'].fillna(agemean, inplace=True)
df['Salary'].fillna(salarymean, inplace=True)
print("\n\n Missing values Replaced with Mean:")
print(df)


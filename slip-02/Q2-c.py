#Q.2 C) Download the heights and weights dataset and load the dataset froma given csv file into a 
#dataframe. Print the first, last 10 rows and random 20 rows also display shape of the  dataset. 

import pandas as pd
df = pd.read_csv("SOCR-HeightWeight.csv")

print("First 10 row:")
print(df.head(10))

print("\nLast 10 rows:")
print(df.tail(10))

print("\nRandom 20 rows:")
print(df.sample(20))

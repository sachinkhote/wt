# A) Write a Python program to create a Pie plot to get the frequency of the three species of 
# the Iris data (Use iris.csv) 
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("iris.csv")

df['Species'].value_counts().plot.pie(explode=[0.1,0.1,0.1],autopct='%1.1f%%',shadow=True)
plt.title("Iris Species %")
plt.show()

#Q.2 B) Write a Python program to generate a line plot of name Vs salary 
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Data.csv")

names = df['Country']
salary = df['Salary']

plt.plot(names, salary, marker='o', linestyle='-', color='b')
plt.title('Name vs Salary')
plt.xlabel('Name')
plt.ylabel('Salary')
plt.show()

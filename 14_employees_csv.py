import os
import pandas as pd

BASE = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE, "employees.csv"))

print("Employees from the CSE department:")
print(df[df["Department"] == "CSE"])

print("\nAverage salary:", df["Salary"].mean())

print("\nHighest salary:", df["Salary"].max())
print("Lowest salary :", df["Salary"].min())

print("\nEmployees with salary greater than Rs. 50,000:")
print(df[df["Salary"] > 50000])

print("\nDepartment-wise average salary:")
print(df.groupby("Department")["Salary"].mean())

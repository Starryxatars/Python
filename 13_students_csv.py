import os
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)


BASE = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE, "students.csv"))

print("First 5 records:")
print(df.head())

print("\nLast 5 records:")
print(df.tail())

df["Total"] = df[["Python", "DBMS", "Maths"]].sum(axis=1)
df["Average"] = df["Total"] / 3

print("\nTotal and average marks of each student:")
print(df[["Student_ID", "Name", "Total", "Average"]].round(2))

print("\nStudents whose average marks are greater than 75:")
print(df[df["Average"] > 75].round(2))

print("\nStudent with the highest average:")
print(df.loc[[df["Average"].idxmax()]].round(2))

print("\nAverage marks for each subject:")
print(df[["Python", "DBMS", "Maths"]].mean().round(2))

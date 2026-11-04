import pandas as pd

data = {
    "Employee_ID": [1, 2, 3, 4, 5],
    "Employee_Name": ["Rahul", "Sneha", "Amit", "Priya", "Vikram"],
    "Department": ["CSE", "HR", "Finance", "CSE", "IT"],
    "Salary": [65000, 42000, 55000, 48000, 72000],
    "Experience": [6, 3, 8, 4, 10],
}

df = pd.DataFrame(data)
print("Employee DataFrame:")
print(df)

print("\nEmployees with salary greater than Rs. 50,000:")
print(df[df["Salary"] > 50000])

print("\nAverage salary:", df["Salary"].mean())
print("Highest salary:", df["Salary"].max())

print("\nEmployee with highest experience:")
print(df.loc[df["Experience"].idxmax()])

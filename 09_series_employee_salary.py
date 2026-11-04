import pandas as pd

salary_dict = {"Rahul": 65000, "Sneha": 42000, "Amit": 55000, "Priya": 48000, "Vikram": 72000}
salary = pd.Series(salary_dict)

print("Salary Series:")
print(salary)

print("\nHighest salary:", salary.max(), "(" + salary.idxmax() + ")")
print("Lowest salary :", salary.min(), "(" + salary.idxmin() + ")")
print("Average salary:", salary.mean())

print("\nEmployees earning more than Rs. 50,000:")
print(salary[salary > 50000])

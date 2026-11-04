import os
import pandas as pd

BASE = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE, "patients.csv"))

print("Patients above 60 years:")
print(df[df["Age"] > 60])

print("\nAverage medical expense:", df["Medical_Expense"].mean())

print("\nPatient with the highest medical expense:")
print(df.loc[df["Medical_Expense"].idxmax()])

print("\nNumber of patients for each disease:")
print(df["Disease"].value_counts())

print("\nPatients whose medical expense exceeds Rs. 50,000:")
print(df[df["Medical_Expense"] > 50000])

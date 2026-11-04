import pandas as pd

data = {
    "Patient_ID": [1, 2, 3, 4, 5],
    "Patient_Name": ["Ravi", "Anita", "Suresh", "Lata", "Manoj"],
    "Age": [65, 34, 72, 58, 61],
    "Disease": ["Diabetes", "Fever", "Heart Disease", "Asthma", "Arthritis"],
    "Medical_Charges": [35000, 4000, 120000, 15000, 52000],
}

df = pd.DataFrame(data)
print("Patient DataFrame:")
print(df)

print("\nPatients above 60 years:")
print(df[df["Age"] > 60])

print("\nAverage medical charge:", df["Medical_Charges"].mean())
print("Maximum medical charge:", df["Medical_Charges"].max())

print("\nPatients with medical charges greater than Rs. 50,000:")
print(df[df["Medical_Charges"] > 50000])

import pandas as pd

age_dict = {101: 65, 102: 34, 103: 72, 104: 58, 105: 61, 106: 23}
ages = pd.Series(age_dict)

print("Patient ages:")
print(ages)

print("\nAverage age:", round(ages.mean(), 2))
print("Oldest patient  : ID", ages.idxmax(), "- Age", ages.max())
print("Youngest patient: ID", ages.idxmin(), "- Age", ages.min())

print("\nPatients above 60 years:")
print(ages[ages > 60])

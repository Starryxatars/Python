import pandas as pd

data = {
    "Student_ID": [1, 2, 3, 4, 5, 6],
    "Name": ["Aarav", "Diya", "Kabir", "Meera", "Rohan", "Sana"],
    "Department": ["CSE", "ECE", "CSE", "IT", "ME", "IT"],
    "Total_Classes": [100, 100, 100, 100, 100, 100],
    "Classes_Attended": [92, 70, 85, 68, 76, 95],
}

df = pd.DataFrame(data)
df["Attendance_Percentage"] = (df["Classes_Attended"] / df["Total_Classes"]) * 100

print("Attendance DataFrame:")
print(df)

print("\nStudents with attendance below 75%:")
print(df[df["Attendance_Percentage"] < 75])

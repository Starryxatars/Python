import pandas as pd

attendance_dict = {"Aarav": 92, "Diya": 70, "Kabir": 85, "Meera": 68, "Rohan": 96, "Sana": 91}
attendance = pd.Series(attendance_dict)

print("Attendance percentages:")
print(attendance)

print("\nAverage attendance:", round(attendance.mean(), 2))

print("\nStudents with attendance below 75%:")
print(attendance[attendance < 75])

print("\nStudents with attendance above 90%:")
print(attendance[attendance > 90])

print("\nHighest attendance:", attendance.max(), "(" + attendance.idxmax() + ")")

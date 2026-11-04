import pandas as pd

marks_dict = {"Aarav": 85, "Diya": 70, "Kabir": 92, "Meera": 66, "Rohan": 78}
marks = pd.Series(marks_dict)

print("Marks Series:")
print(marks)

print("\nMarks of Kabir:", marks["Kabir"])

print("\nMaximum marks:", marks.max(), "(" + marks.idxmax() + ")")
print("Minimum marks:", marks.min(), "(" + marks.idxmin() + ")")

print("\nAverage marks:", marks.mean())

print("\nStudents who scored more than 75:")
print(marks[marks > 75])

import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)

data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Student_Name": ["Aarav", "Diya", "Kabir", "Meera", "Rohan"],
    "Python_Marks": [85, 70, 92, 66, 78],
    "DBMS_Marks": [80, 65, 88, 70, 82],
    "Maths_Marks": [90, 72, 95, 60, 74],
}

df = pd.DataFrame(data)
print("DataFrame:")
print(df)

df["Total"] = df[["Python_Marks", "DBMS_Marks", "Maths_Marks"]].sum(axis=1)
print("\nTotal marks of each student:")
print(df[["Student_ID", "Student_Name", "Total"]])


df["Average"] = df["Total"] / 3
print("\nAverage marks:")
print(df[["Student_ID", "Student_Name", "Average"]].round(2))

print("\nStudents with average above 75%:")
print(df[df["Average"] > 75].round(2))

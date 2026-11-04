import numpy as np

marks = np.array([78, 85, 92, 67, 74, 88, 95, 60, 81, 70])
print("Marks of 10 students:", marks)

print("Highest marks     :", marks.max())
print("Lowest marks      :", marks.min())
print("Average marks     :", marks.mean())
print("Median            :", np.median(marks))
print("Standard deviation:", round(marks.std(), 2))

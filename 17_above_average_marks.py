import numpy as np

marks = np.array([72, 85, 91, 64, 78, 88, 95, 55, 69, 83,
                  77, 90, 62, 81, 74, 98, 59, 86, 70, 93])

average = marks.mean()

print("Marks of 20 students:", marks)
print("Class average       :", average)
print("Marks above average :", marks[marks > average])

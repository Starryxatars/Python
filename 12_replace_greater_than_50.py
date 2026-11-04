import numpy as np

arr = np.array([12, 55, 78, 23, 90, 41, 67, 8, 50, 63])
print("Original array:", arr)

arr[arr > 50] = 0
print("After replacing elements > 50 with 0:", arr)

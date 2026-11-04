import numpy as np

arr = np.array([42, 7, 19, 88, 3, 56, 21, 74])
print("Unsorted array  :", arr)

ascending = np.sort(arr)
descending = np.sort(arr)[::-1]

print("Ascending order :", ascending)
print("Descending order:", descending)

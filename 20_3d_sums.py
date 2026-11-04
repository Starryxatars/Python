import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)
print("3D array (2, 3, 4):\n", arr)

print("\nSum of all elements:", arr.sum())
print("\nSum of each layer  :", arr.sum(axis=(1, 2)))
print("\nSum along rows (axis=2):\n", arr.sum(axis=2))
print("\nSum along columns (axis=1):\n", arr.sum(axis=1))

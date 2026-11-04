import numpy as np

arr = np.arange(1, 28).reshape(3, 3, 3)
flat = arr.flatten()

print("3D array:\n", arr)
print("\nFlattened array:", flat)

print("\nSum    :", flat.sum())
print("Average:", flat.mean())
print("Maximum:", flat.max())
print("Minimum:", flat.min())

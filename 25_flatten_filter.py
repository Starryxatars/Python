import numpy as np

arr = np.random.randint(1, 101, size=(3, 4, 5))
flat = arr.flatten()
average = flat.mean()

print("Random 3D array (3, 4, 5):\n", arr)
print("\nFlattened array:", flat)
print("Average value  :", average)

print("\nElements greater than 50:", flat[flat > 50])
print("Even numbers            :", flat[flat % 2 == 0])
print("Elements less than average:", flat[flat < average])

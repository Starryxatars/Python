import numpy as np

arr = np.random.randint(1, 101, size=(3, 4, 5))
print("Random 3D array (3, 4, 5):\n", arr)

print("\nMean              :", arr.mean())
print("Median            :", np.median(arr))
print("Standard deviation:", arr.std())
print("Variance          :", arr.var())
print("Minimum           :", arr.min())
print("Maximum           :", arr.max())

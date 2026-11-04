import numpy as np

matrix = np.arange(1, 17).reshape(4, 4)
print("4 x 4 matrix:\n", matrix)

print("\nSum of each row   :", matrix.sum(axis=1))
print("Sum of each column:", matrix.sum(axis=0))

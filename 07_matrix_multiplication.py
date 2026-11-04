import numpy as np


A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[7, 8],
              [9, 10],
              [11, 12]])

print("Matrix A (2x3):\n", A)
print("\nMatrix B (3x2):\n", B)
print("\nMatrix multiplication (np.dot):\n", np.dot(A, B))
print("\nMatrix multiplication (np.matmul):\n", np.matmul(A, B))

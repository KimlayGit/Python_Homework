import numpy as np

# =========================
# Task 1 
# =========================
print("=== Task 1 ===")
arr = np.random.randint(1, 51, size=15)
print("Array:", arr)
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Min:", np.min(arr))
print("Max:", np.max(arr))
print("Standard Deviation:", np.std(arr))

# =========================
# Task 2 
# =========================
print("\n=== Task 2 ===")
matrix = np.random.randint(1, 10, size=(4, 4))
print("Matrix:\n", matrix)

det = np.linalg.det(matrix)
transpose = matrix.T

print("Determinant:", det)
print("Transpose:\n", transpose)


if det != 0:
    inverse = np.linalg.inv(matrix)
    print("Inverse:\n", inverse)
else:
    print("Inverse: Not possible (determinant = 0)")

# =========================
# Task 3 
# =========================
print("\n=== Task 3 ===")
original = np.random.rand(10)
shuffled = original.copy()
np.random.shuffle(shuffled)

print("Original Array:", original)
print("Shuffled Array:", shuffled)

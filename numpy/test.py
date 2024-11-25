import numpy as np

# 1. Array Creation
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.zeros((3, 3))
arr3 = np.ones((2, 4))
arr4 = np.arange(0, 10, 2)
arr5 = np.linspace(0, 1, 5)

# 2. Array Operations
math_ops = np.array([1, 2, 3])
print(math_ops + 2)  # Addition
print(math_ops * 3)  # Multiplication
print(np.sqrt(math_ops))  # Square root
print(np.exp(math_ops))  # Exponential

# 3. Array Reshaping
matrix = np.array([1, 2, 3, 4, 5, 6])
reshaped = matrix.reshape(2, 3)
transposed = reshaped.T

# 4. Linear Algebra
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
dot_product = np.dot(A, B)
eigenvalues = np.linalg.eigvals(A)

# 5. Statistics
data = np.array([1, 2, 3, 4, 5])
mean = np.mean(data)
std = np.std(data)
var = np.var(data)
median = np.median(data)

# 6. Boolean Indexing
arr = np.array([1, 2, 3, 4, 5])
mask = arr > 2
filtered = arr[mask]

# 7. Random Numbers
random_array = np.random.rand(3, 3)
normal_dist = np.random.normal(0, 1, 1000)

# 8. Broadcasting
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([10, 20, 30])
result = a + b

# 9. Matrix Operations
matrix_inv = np.linalg.inv(A)
determinant = np.linalg.det(A)

# 10. Saving & Loading
np.save('array.npy', arr1)
loaded_arr = np.load('array.npy')
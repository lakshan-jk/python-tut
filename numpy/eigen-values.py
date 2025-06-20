import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

c = np.dot(A, B)

# np.linalg.eig() returns two values:
#   1. eigenvalues - a 1D array of eigenvalues of the input matrix
#   2. eigenvectors - a 2D array of eigenvectors of the input matrix,
#  where the i-th column is the egvectior corresponding to the i-th eigenvalue
eigenvalues, eigenvectors = np.linalg.eig(c)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)

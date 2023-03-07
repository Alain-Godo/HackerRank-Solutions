import numpy as np

n,m = list(map(int,input().split()))

matrix1 = np.array([list(map(int,input().split())) for i in range(n)])
matrix2 = np.array([list(map(int,input().split())) for i in range(n)])

print(matrix1 + matrix2)
print(matrix1 - matrix2)
print(matrix1 * matrix2)
print(matrix1 // matrix2)
print(matrix1 % matrix2)
print(matrix1 ** matrix2)
import numpy as np

n = int(input())

matrix1 = np.array([list(map(int,input().split())) for i in range(n)])
matrix2 = np.array([list(map(int,input().split())) for i in range(n)])
print(matrix1.dot(matrix2))

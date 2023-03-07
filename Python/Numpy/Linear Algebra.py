import numpy as np

n = int(input())

matrix = np.array([list(map(float,input().split())) for i in range(n)])

print(round(np.linalg.det(matrix),2))
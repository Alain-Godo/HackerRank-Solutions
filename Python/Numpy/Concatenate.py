import numpy as np

n,m,p = list(map(int,input().split()))

matrix1 = [list(map(int,input().split())) for i in range(n)]
matrix2 = [list(map(int,input().split())) for i in range(m)]

print(np.concatenate((np.array(matrix1),np.array(matrix2))))
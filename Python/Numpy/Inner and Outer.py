import numpy as np

matrix1 = np.array(list(map(int,input().split())))
matrix2 = np.array(list(map(int,input().split())))
print(np.inner(matrix1,matrix2),np.outer(matrix1,matrix2),sep="\n")

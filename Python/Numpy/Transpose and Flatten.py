import numpy as np

n,m = list(map(int,input().split()))

matrix = [list(map(int,input().split())) for i in range(n)]
print(np.array(matrix).transpose(),np.array(matrix).flatten(),sep="\n")


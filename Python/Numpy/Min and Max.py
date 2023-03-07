import numpy as np

n,m = list(map(int,input().split()))
arr = np.array([list(map(int,input().split())) for i in range(n)])
print(np.max(arr.min(1)))

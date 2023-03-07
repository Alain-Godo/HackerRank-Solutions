import numpy as np

n,m = list(map(int,input().split()))
arr = np.array([list(map(float,input().split())) for i in range(n)])
print(arr.mean(1),arr.var(0),np.std(arr,axis=None).round(11),sep="\n",end="")
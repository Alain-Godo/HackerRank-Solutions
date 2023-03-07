import numpy as np

dim = tuple(map(int,input().split()))

print(np.zeros(dim,dtype=np.int8),np.ones(dim,dtype=np.int8),sep="\n")

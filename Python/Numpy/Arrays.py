import numpy as np

def arrays(arr):
    n_a = np.array(arr)
    return n_a[::-1] 

arr = list(map(float,input().strip().split(' ')))
print(arrays(arr))
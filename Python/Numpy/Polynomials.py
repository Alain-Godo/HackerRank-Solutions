import numpy as np

pol = np.array(list(map(float,input().split())))
print(np.polyval(pol,float(input())))
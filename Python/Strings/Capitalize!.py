#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    r = ''
    e = True
    
    for w in s:
        if e:    
            r += (w if w.isdigit() else w.upper())
            e = False
        else:
            r += w
        if w == " ":
            e = True 
            
    return r   
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

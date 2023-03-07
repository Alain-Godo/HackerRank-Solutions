"""
n, x = list(map(int,input().split()))

sum = [0]*n

for subj in range(x):
    stud = list(map(float,input().split()))
    for i,note in enumerate(stud):
        sum[i] += note

print(*[acum/x for acum in sum],sep="\n",end="")
"""

n, x = list(map(int,input().split()))

suma = []

for notes in zip(*[list(map(float,input().split())) for i in range(x)]):
    suma.append(sum(notes))

print(*[acum/x for acum in suma],sep="\n",end="")
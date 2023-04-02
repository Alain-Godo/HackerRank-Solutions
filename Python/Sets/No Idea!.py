n, m = list(map(int,input().split()))

fr = {}
for e in list(map(int,input().split())):
    fr[e] = fr.setdefault(e,0) + 1

set_A = set(list(map(int,input().split())))
set_B = set(list(map(int,input().split())))

points = 0
for k,v in fr.items():
    if k in set_A:
        points += v
    if k in set_B:
        points -= v

print(points)


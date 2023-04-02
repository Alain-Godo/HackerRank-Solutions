n = int(input())
s1 = set(map(int,input().split()))

m = int(input())
s2 = set(map(int,input().split()))

sym_diff = s1.union(s2)
for e in s1.intersection(s2):
    sym_diff.discard(e)

print(*sorted(list(sym_diff)),sep = "\n")
import itertools

data = input().split()

for e in list(itertools.permutations(sorted(data[0]), int(data[1]))):
    print(*e, sep="")

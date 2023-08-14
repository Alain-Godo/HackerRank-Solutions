from itertools import groupby

for num, group in groupby(map(int, input()), lambda x: x):
    print(f"({len(list(group))}, {num})", end=" ")

from itertools import combinations

n, l, k = input(), input().split(), int(input())
a_cases, t_cases = 0, 0

for element in combinations(l, k):
    t_cases += 1
    if "a" in element:
        a_cases += 1
print(a_cases/t_cases)

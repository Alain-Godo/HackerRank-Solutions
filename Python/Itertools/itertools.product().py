import itertools

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

print(*list(itertools.product(l1, l2)))

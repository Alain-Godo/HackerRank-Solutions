import itertools

word, r = input().split()

for i in range(1, int(r)+1):
    for element in itertools.combinations(sorted(word), int(i)):
        print(*element, sep="")

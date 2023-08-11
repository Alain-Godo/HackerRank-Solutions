import itertools

word, r = input().split()

for element in itertools.combinations_with_replacement(sorted(word), int(r)):
    print(*element, sep="")

DIFF = 10000

def f(x):
    rank = 0
    if x.isupper():
        rank = DIFF
    elif x.isdigit():
        rank = 2*DIFF
        if int(x)%2 == 0:
            rank = 3*DIFF
    return rank + ord(x)

print("".join(sorted(input(),key = lambda x: f(x))))
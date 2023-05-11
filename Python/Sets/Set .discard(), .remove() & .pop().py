n = int(input())
s = set(map(int, input().split()))

nc = int(input())

for i in range(nc):
    c = input().split()
    
    if c[0] == "pop":
        s.pop()
    elif c[0] == "remove":
        s.remove(int(c[1]))
    else:
        s.discard(int(c[1]))
        
print(sum(s))
    
    
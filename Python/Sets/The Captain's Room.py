n = input()
l = input().split()
s_saw = set()
s_new = set()

for e in l:
    if e in s_saw:
        s_new.discard(e)
    else:
        s_new.add(e)
        s_saw.add(e)
        
print(*s_new)
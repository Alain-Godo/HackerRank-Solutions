n = input()
s1 = set(map(int,input().split()))
t = int(input())

while 2*t:
    operation = input().split()
    s2 = set(map(int,input().split()))
    
    if operation[0] == "intersection_update":
        s1.intersection_update(s2)
    elif operation[0] == "update":
        s1.update(s2)
    elif operation[0] == "symmetric_difference_update":
        s1.symmetric_difference_update(s2)
    else:
        s1.difference_update(s2)
        
    t-=1

print(sum(s1))
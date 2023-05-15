t = int(input())

while t!=0:
    n1 = int(input())
    s1 = set(map(int,input().split()))
    
    n2 = int(input())
    s2 = set(map(int,input().split()))
    
    print(["False","True"][len(s1 & s2) == len(s1)])
    #print(["False","True"][s1.issubset(s2)])
    
    t-=1
    
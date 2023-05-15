s1 = set(map(int,input().split()))
t = int(input())
answer = True

while t!=0:
    new_s = set(map(int,input().split()))
    
    if not((len(s1 & new_s) == len(new_s)) and (len(new_s)<len(s1))):
    #if not s1.issuperset(new_s):
         answer = False
    t-=1
    
print(["False","True"][answer])
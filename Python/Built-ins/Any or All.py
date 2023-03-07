n,nums = input(),input().split()
print(any(list(map(lambda x: x == x[::-1] ,nums))) and all(list(map(lambda x: int(x)>=0 ,nums))))

def painter(n,m):
    # Top figure
    for i in range(n//2):
        print((".|."*(2*i + 1)).center(m,'-'))

    # Center
    print("WELCOME".center(m,'-'))

    # Bottom figure 
    for i in range(n//2 -1 ,-1,-1):
        print((".|."*(2*i + 1)).center(m,'-'))

n,m = list(map(int,input().split()))
painter(n,m)
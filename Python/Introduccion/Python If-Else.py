if __name__ == '__main__':
    n = int(input().strip())
    label = "Weird"
    
    if ((n & 1) == 0) and ((2<=n<=5) or (n>20)):
        label = "Not Weird"
    
    print(label)
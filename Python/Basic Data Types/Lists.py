if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        operation = input().split()
        if operation[0] == "print":
            print(l)
        elif operation[0] == "insert":
            l.insert(int(operation[1]),int(operation[2]))
        elif operation[0] == "remove":
            l.remove(int(operation[1]))
        elif operation[0] == "append":
            l.append(int(operation[1]))
        elif operation[0] == "pop":
            l.pop()
        elif operation[0] == "reverse":
            l.reverse()
        elif operation[0] == "sort":
            l.sort()    
        
cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    f = [0,1]
    if n <= 2:
        return f[:n]
    else:
        for i in range(2,n):
            f.append(f[i-1] + f[i-2])
        return f

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
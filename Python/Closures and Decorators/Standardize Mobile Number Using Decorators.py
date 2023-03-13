def wrapper(f):
    def fun(l):
        new_l = [f'+91 {n[-10:-5]} {n[-5:]}' for n in l]
        f(new_l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

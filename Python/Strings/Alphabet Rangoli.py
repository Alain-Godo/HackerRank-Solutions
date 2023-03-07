def print_rangoli(size):
    # Center
    aux1 = [chr(ord('a') + i) for i in range(size - 1,0,-1)]
    aux2 = [chr(ord('a') + i) for i in range(1,size)]
    center = "-".join(aux1) + "-a-" + "-".join(aux2)
    width = len(center)
    
    # Top figure
    for i in range(size-1):
        aux1 = [chr(ord('a') + i) for i in range(size - 1,size-1 - i,-1)]
        aux2 = [chr(ord('a') + i) for i in range(size - i,size)]  
        print(("-".join(aux1) + "-" + chr(ord('a') + size-1 - i) + "-"\
              + "-".join(aux2)).center(width,'-'))  
        
    print(center if size>1 else center.replace("-",""))

    # Bottom figure
    for i in range(size-2,-1,-1):
        aux1 = [chr(ord('a') + i) for i in range(size - 1,size-1 - i,-1)]
        aux2 = [chr(ord('a') + i) for i in range(size- i,size)]  
        print(("-".join(aux1) + "-" + chr(ord('a') + size-1 - i) + "-"\
              + "-".join(aux2)).center(width,'-'))  

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
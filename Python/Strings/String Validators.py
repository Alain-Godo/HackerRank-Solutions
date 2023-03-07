def checker(s):
    chk_list = [False]*5
    
    chk_list[0] = any(map(str.isalnum,s))
    chk_list[1] = any(map(str.isalpha,s))
    chk_list[2] = any(map(str.isdigit,s))
    chk_list[3] = any(map(str.islower,s))
    chk_list[4] = any(map(str.isupper,s))
    
    return chk_list

if __name__ == '__main__':
    s = input()
    print(*checker(s),sep='\n')

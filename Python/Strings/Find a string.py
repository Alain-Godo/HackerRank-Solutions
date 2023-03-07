def count_substring(string, sub_string):
    c = 0
    if sub_string:
        for i in range(len(string) - len(sub_string) + 1):
            if string.find(sub_string,i,i+len(sub_string)) != -1:
                c += 1
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
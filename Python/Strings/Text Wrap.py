import textwrap

def wrap(string, max_width):
    r = ""
    for i in range(0,len(string),max_width):
        if i + max_width-1 <= len(string)-1:
            r += string[i:i+max_width]
        else:
            r += string[i:]
        r += '\n'

    # return "\n".join(textwrap.wrap(string,max_width))	 
    return r

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
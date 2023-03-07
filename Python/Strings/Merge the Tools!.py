from textwrap import wrap

def merge_the_tools(string, k):
    for v in wrap(string,k):
        print(''.join(dict.fromkeys(v)))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
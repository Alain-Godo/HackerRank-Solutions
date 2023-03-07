def print_formatted(number):
    r = ""
    w = len(bin(number).lstrip('0b'))
    for i in range(1,number+1):
        decimal = str(i)
        octal = oct(i).lstrip('0o')
        hexadecimal = "".join(map(str.upper,hex(i).lstrip('0x')))
        binary = bin(i).lstrip('0b')
        r += decimal.rjust(w) + octal.rjust(w+1) + hexadecimal.rjust(w+1) +\
        binary.rjust(w+1) + "\n"
    print(r)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
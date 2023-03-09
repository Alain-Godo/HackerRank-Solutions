import re

def fun(s):
    evalaluation = re.fullmatch("([\-_a-zA-Z0-9]+)@([a-zA-Z0-9]+)\.[a-zA-Z]{1,3}",s) 
    return True if evalaluation else False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
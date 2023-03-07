x,k = input().split()
exp = list(map(lambda y: y.replace("x",x),input().split(" + ")))

fx = sum(eval(i) for i in exp)

print(["False","True",][fx==int(k)])


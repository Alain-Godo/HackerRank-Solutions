if __name__ == '__main__':
    l = []
    scores = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name,score])
        scores.add(score) 
    l.sort(key=lambda x: (x[1],x[0]))
    s = sorted(scores)
    print(*(e[0] for e in l if e[1]==s[1]),sep="\n")
    
         
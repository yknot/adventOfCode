input = open('input').read()


xS = 0
yS = 0
xR = 0
yR = 0

visited = set()

visited.add((0,0))

f = 1
for l in input:
    if l == '^':
        if f:
            yS+=1
        else:
            yR+=1
    elif l == '>':
        if f:
            xS+=1
        else:
            xR+=1
    elif l == 'v':
        if f:
            yS-=1
        else:
            yR-=1
    elif l == '<':
        if f:
            xS-=1
        else:
            xR-=1
    if f:
        visited.add((xS,yS))
        f = 0
    else:
        visited.add((xR,yR))
        f = 1


print len(visited)
        

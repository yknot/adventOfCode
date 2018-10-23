data = [o.strip().split() for o in open('input').readlines()]

final = {}
parsed = {}
for d in data:
    parsed[d[0]] = (int(d[3]), int(d[6]), int(d[-2]))
    final[d[0]] = 0


finish = 2503
for i in range(1,finish+1):
    thisRound = []
    for name, val in parsed.items():
        time = val[1] + val[2]
        reps = i/time
        rem = i%time


        # if you are resting
        if time - rem <= val[2]:
            thisRound.append((name,val[0]*val[1]*(reps+1)))
        # else if you are in the middle of traveling
        else:
            thisRound.append((name,val[0]*val[1]*reps+(rem*val[0])))

    thisRound = sorted(thisRound, key=lambda x: x[1], reverse=True)
    for t in thisRound:
        if t[1] == thisRound[0][1]:
            final[t[0]] += 1

    
    
print max(final.values())

data = [o.strip().split() for o in open('input').readlines()]


parsed = {}
for d in data:
    parsed[d[0]] = (int(d[3]), int(d[6]), int(d[-2]))

final = {}
finish = 2503
for name, val in parsed.items():
    time = val[1] + val[2]
    reps = finish/time
    rem = finish%time

    # if you are resting
    if time - rem > val[1]:
        final[name] = val[0]*val[1]*(reps+1)
    # else if you are in the middle of traveling
    else:
        final[name] = val[0]*val[1]*reps+(time - rem)*val[0]


assert(max(final.values()) == 2660)
print max(final.values())



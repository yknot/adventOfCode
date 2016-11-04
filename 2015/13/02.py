data = [o.strip()[:-1].split() for o in open('input').readlines()]

# parse data
people = {}
happiness = {}
for d in data:
    if d[2] == 'gain':
        val = int(d[3])
    else:
        val = int(d[3])*-1
    people[d[0]] = 0
    happiness[(d[0], d[-1])] = val

people['me'] = 0
for p in people.keys():
    happiness[('me', p)] = 0
    happiness[(p, 'me')] = 0


def TSP(current, people, total, best, first):
    people[current] = 1
    if sum(people.values()) == len(people.values()):
        total += happiness[(current,first)]
        total += happiness[(first,current)]
        if total > best:
            best = total
        return best

    for edge in happiness.keys():
        if current in edge:
            loc = edge.index(current)
            if people[edge[loc-1]] != 1:
                best = TSP(edge[loc-1], people, total + happiness[edge] + happiness[(edge[1], edge[0])], best, first)
                people[edge[loc-1]] = 0

    return best


bests = []
for p in people.keys():
    print p
    bests.append(TSP(p, people, 0, -9999999, p))
    people[p] = 0


print max(bests)


def TSP(current, cities, total, best):
    cities[current] = 1
    if sum(cities.values()) == len(cities.values()):
        if total > best:
            best = total
        return best

    for edge in dists.keys():
        if current in edge:
            loc = edge.index(current)
            if cities[edge[loc-1]] != 1:
                best = TSP(edge[loc-1], cities, total + dists[edge], best)
                cities[edge[loc-1]] = 0

    return best


data = [l.strip() for l in open('input').readlines()]

# read in data
dists = {}
cities = {}
for d in data:
    d = d.split()
    start = d[0]
    end = d[2]
    dist = int(d[4])
    # cities stores visited
    cities[start] = 0
    cities[end] = 0
    # dists stores graph
    dists[(start, end)] = dist

bests = []
for c in cities.keys():
    bests.append(TSP(c, cities, 0, 0))
    cities[c] = 0


print max(bests)

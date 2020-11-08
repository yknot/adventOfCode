from collections import defaultdict

inpt = [i for i in open("02_input")]

twos = 0
threes = 0

for line in inpt:
    counts = defaultdict(int)
    for l in line:
        counts[l] += 1

    if 2 in counts.values():
        twos += 1
    if 3 in counts.values():
        threes += 1

assert twos * threes == 5390

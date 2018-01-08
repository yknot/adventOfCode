import numpy as np

raw = open('input').read().splitlines()
counts = np.zeros(len(raw))

for i, r in enumerate(raw):
    dirs = r.split()[2].split('<')[1][:-1].split(',')
    total = 0
    for d in dirs:
        total += abs(int(d))
    counts[i] = total


# closest will be one with minimum acceleration
print(np.argmin(counts))

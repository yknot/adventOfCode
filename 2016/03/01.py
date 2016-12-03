import numpy as np

triangles = np.loadtxt('input')
combinations = [(0, 1, 2),
                (0, 2, 1),
                (1, 2, 0)]

total = 0
for t in triangles:
    possible = True
    for a, b, c in combinations:
        if t[a] + t[b] <= t[c]:
            possible = False
            break

    if possible:
        total += 1

print(total)

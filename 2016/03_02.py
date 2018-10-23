import numpy as np

triangles = np.loadtxt('input').T
combinations = [(0, 1, 2),
                (0, 2, 1),
                (1, 2, 0)]

total = 0
for row in triangles:
    for start in range(len(row)//3):
        i = start * 3
        t = row[i:i+3]
        possible = True
        for a, b, c in combinations:
            if t[a] + t[b] <= t[c]:
                possible = False
                break

        if possible:
            total += 1

print(total)

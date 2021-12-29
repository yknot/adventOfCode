"""
Day 15, part 2
"""
from copy import deepcopy
from collections import defaultdict
import numpy as np
from utils import read_input


def expand_grid(inpt):
    grid_copy = deepcopy(inpt)

    for _ in range(4):
        for i in range(len(grid_copy)):
            for j in range(len(grid_copy[i])):
                grid_copy[i][j] += 1
                if grid_copy[i][j] == 10:
                    grid_copy[i][j] = 1
        inpt += deepcopy(grid_copy)

    for i, row in enumerate(inpt):
        row_copy = row.copy()
        for _ in range(4):
            for j, _ in enumerate(row_copy):
                row_copy[j] += 1
                if row_copy[j] == 10:
                    row_copy[j] = 1
            inpt[i] += row_copy.copy()

    return inpt


def dijkstra(grid, edges, size):
    queue = []
    visited = set()
    dist = {}
    prev = {}

    for k in grid.keys():
        dist[k] = np.inf
        prev[k] = None
    dist[(0, 0)] = 0
    queue.append((0, 0))

    next_min_point = None
    next_min_val = None

    while queue:
        min_point = None
        min_val = np.inf
        for q in queue:
            if dist[q] < min_val:
                min_val = dist[q]
                min_point = q

        # remove from queue
        queue.pop(queue.index(min_point))

        # hit end
        if min_point == (size - 1, size - 1):
            break

        for i, j in edges[min_point]:
            if (i, j) not in visited:
                alt = dist[min_point] + grid[(i, j)]
                if alt < dist[(i, j)]:
                    dist[(i, j)] = alt
                    prev[(i, j)] = min_point
                if (i, j) not in queue:
                    queue.append((i, j))

        visited.add(min_point)

    return dist, prev


def find_path(inpt):
    inpt = expand_grid(inpt)

    grid = {}
    edges = defaultdict(list)
    for i in range(len(inpt)):
        for j in range(len(inpt[i])):
            grid[(i, j)] = inpt[i][j]
            if i > 0:
                edges[(i, j)].append((i - 1, j))
            if j > 0:
                edges[(i, j)].append((i, j - 1))
            if i < (len(inpt) - 1):
                edges[(i, j)].append((i + 1, j))
            if j < (len(inpt[i]) - 1):
                edges[(i, j)].append((i, j + 1))

    dist, _ = dijkstra(grid, edges, len(inpt))
    target = (len(inpt) - 1, len(inpt[0]) - 1)

    return dist[target]


def parser(line):
    return [int(i) for i in list(line.strip())]


test_inpt = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

test_inpt = [parser(line) for line in test_inpt.split("\n")]
assert find_path(deepcopy(test_inpt)) == 315


inpt = list(read_input(15, line_parser=parser))
try:
    res = find_path(inpt)
    assert res == 2979
except:
    print(res)
    raise

"""
Day 12
"""
import numpy as np
from heapq import heappop, heappush
from itertools import count
from collections import defaultdict
from utils import read_input


class PriorityQueue:
    def __init__(self):
        self.pq = []
        self.entry_finder = {}
        self.removed_placeholder = "<removed-task>"
        self.counter = count()

    def add(self, task, priority=0):
        if task in self.entry_finder:
            self.remove(task)
        n = next(self.counter)
        entry = [priority, n, task]
        self.entry_finder[task] = entry
        heappush(self.pq, entry)

    def remove(self, task):
        entry = self.entry_finder.pop(task)
        entry[-1] = self.removed_placeholder

    def pop(self):
        while self.pq:
            _, _, task = heappop(self.pq)
            if task is not self.removed_placeholder:
                del self.entry_finder[task]
                return task
        raise KeyError("empty queue")

    def __len__(self):
        return len(self.pq)

    def __contains__(self, task):
        return task in self.entry_finder.keys()


def dijkstra(grid, edges, start, target):
    queue = PriorityQueue()
    dist = {}
    prev = {}

    dist[start] = 0
    queue.add(start, dist[start])
    for k in grid.keys():
        if k != start:
            dist[k] = np.inf
            prev[k] = None

    while len(queue):
        min_point = queue.pop()
        # hit end
        if min_point == target:
            break

        for i, j in edges[min_point]:
            alt = dist[min_point] + grid[(i, j)]
            if alt < dist[(i, j)]:
                dist[(i, j)] = alt
                prev[(i, j)] = min_point
                queue.add((i, j), alt)

    return dist, prev


def find_shortest_path(inpt):
    inpt = [list(l) for l in inpt]
    grid = {}
    edges = defaultdict(list)
    starts, target = [], None
    for i, line in enumerate(inpt):
        for j, elem in enumerate(line):
            if elem == "S" or elem == "a":
                starts.append((i, j))
                inpt[i][j] = "a"
            if elem == "E":
                target = (i, j)
                inpt[i][j] = "z"

    for i, line in enumerate(inpt):
        for j, elem in enumerate(line):

            grid[(i, j)] = 1
            if i > 0 and (ord(elem) + 1) >= ord(inpt[i - 1][j]):
                edges[(i, j)].append((i - 1, j))
            if j > 0 and (ord(elem) + 1) >= ord(inpt[i][j - 1]):
                edges[(i, j)].append((i, j - 1))
            if i < (len(inpt) - 1) and (ord(elem) + 1) >= ord(inpt[i + 1][j]):
                edges[(i, j)].append((i + 1, j))
            if j < (len(inpt[i]) - 1) and (ord(elem) + 1) >= ord(inpt[i][j + 1]):
                edges[(i, j)].append((i, j + 1))

    dists = []
    for start in starts:
        dist, _ = dijkstra(grid, edges, start, target)
        dists.append(dist[target])

    return min(dists)


test_inpt = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


assert find_shortest_path(test_inpt.split("\n")) == 29

inpt = list(read_input(12))

assert find_shortest_path(inpt) == 388

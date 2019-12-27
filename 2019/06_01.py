"""
Day 6

create the graph and count the orbits

"""

from collections import defaultdict
from utils import read_input


parse_input = lambda x: [l.split(")") for l in x]


def create_graph(edges):
    "create the directed graph from edges"
    graph = defaultdict(list)

    for x, y in edges:
        graph[x].append(y)

    return graph


def count_orbits(graph, key="COM", depth=0):
    "count orbits"
    if key not in graph:
        return depth

    total = 0
    for n in graph[key]:
        total += count_orbits(graph, n, depth + 1)

    return total + depth


test = ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L"]

assert count_orbits(create_graph(parse_input(test))) == 42


print(count_orbits(create_graph(parse_input(read_input(6)))))

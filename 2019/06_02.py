"""
Day 6 part 2

create the graph and count the orbits

"""

from collections import defaultdict
from utils import read_input


parse_input = lambda x: [l.split(")") for l in x]


def create_graph(edges):
    "create the directed graph from edges"
    graph = {}

    for x, y in edges:
        graph[y] = x

    return graph


def count_orbits(graph):
    "count transfers"
    # get paths
    path_you = []
    cur_key = "YOU"
    while cur_key != "COM":
        cur_key = graph[cur_key]
        path_you.append(cur_key)

    path_san = []
    cur_key = "SAN"
    while cur_key != "COM":
        cur_key = graph[cur_key]
        path_san.append(cur_key)

    # reverse
    path_you = path_you[::-1]
    path_san = path_san[::-1]

    # iterate
    i = 0
    while path_you[i] == path_san[i]:
        i += 1

    return (len(path_you) - i) + (len(path_san) - i)


test = [
    "COM)B",
    "B)C",
    "C)D",
    "D)E",
    "E)F",
    "B)G",
    "G)H",
    "D)I",
    "E)J",
    "J)K",
    "K)L",
    "K)YOU",
    "I)SAN",
]

assert count_orbits(create_graph(parse_input(test))) == 4


assert count_orbits(create_graph(parse_input(read_input(6)))) == 520

"""
Day 12
"""
from copy import copy
from collections import defaultdict
from utils import read_input


def create_connections(pairs):
    connections = defaultdict(list)
    for a, b in pairs:
        connections[a].append(b)
        connections[b].append(a)

    return connections


def recurse_paths(connections, path):
    tot = 0
    curr_node = path[-1]
    if curr_node == "end":
        return 1

    for b in connections[curr_node]:
        if b not in path or b.isupper():
            new_path = copy(path)
            new_path.append(b)
            tot += recurse_paths(connections, new_path)

    return tot


def find_paths(pairs):
    connections = create_connections(pairs)

    tot = recurse_paths(connections, ["start"])
    return tot


def parser(line):
    return line.strip().split("-")


test_inpt = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

test_inpt = [parser(line) for line in test_inpt.split()]
assert find_paths(test_inpt) == 10

test_inpt = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

test_inpt = [parser(line) for line in test_inpt.split()]
assert find_paths(test_inpt) == 19

inpt = list(read_input(12, line_parser=parser))
assert find_paths(inpt) == 3576

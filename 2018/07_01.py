"""
Day 7 part 1
"""
from collections import defaultdict
from utils import read_input, flatten


def order(pairs):
    edges = defaultdict(list)
    nodes = set()
    for a, b in pairs:
        edges[a].append(b)
        nodes.add(a)
        nodes.add(b)

    queue = sorted(nodes.difference(set(flatten(edges.values()))))
    out = ""

    while len(nodes) > 1:
        # get the next one and add to output
        q = queue.pop(0)
        out += q
        # delete since it's been put int the output
        del edges[q]
        nodes.remove(q)

        # resort queue
        queue = sorted(nodes.difference(set(flatten(edges.values()))))

    out += queue[0]
    return out


def parser(line):
    splits = line.split(" ")
    return (splits[1], splits[7])


test_inpt = (
    ("C", "A"),
    ("C", "F"),
    ("A", "B"),
    ("A", "D"),
    ("B", "E"),
    ("D", "E"),
    ("F", "E"),
)


assert order(test_inpt) == "CABDFE"

inpt = read_input(7, line_parser=parser)

assert order(inpt) == "JMQZELVYXTIGPHFNSOADKWBRUC"

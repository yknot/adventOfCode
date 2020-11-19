"""
Day 7 part 2
"""
from collections import defaultdict
from utils import read_input, flatten


def create_nodes_edges(pairs):
    edges = defaultdict(list)
    nodes = set()
    for a, b in pairs:
        edges[a].append(b)
        nodes.add(a)
        nodes.add(b)

    return nodes, edges


def order(pairs, n_workers, delay):
    nodes, edges = create_nodes_edges(pairs)

    queue = sorted(nodes.difference(set(flatten(edges.values()))))
    out = ""
    workers = [0] * n_workers
    workers_letter = [""] * n_workers

    steps = 0

    while len(edges) or sum(workers) != 0:
        # zero out done workers
        for i, _ in enumerate(workers):
            if workers[i] > 0:
                workers[i] -= 1
            if workers[i] == 0 and workers_letter[i]:
                out += workers_letter[i]
                # delete since it's been put int the output
                if workers_letter[i] in edges:
                    del edges[workers_letter[i]]
                workers_letter[i] = ""
        # reset the queue
        queue = sorted(nodes.difference(set(flatten(edges.values()))))

        # add jobs if available
        for i, _ in enumerate(workers):
            if workers[i] == 0 and len(queue):
                q = queue.pop(0)
                workers[i] = delay + ord(q) - 64
                workers_letter[i] = q
                nodes.remove(q)

        steps += 1

    return steps - 1


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


assert order(test_inpt, n_workers=2, delay=0) == 15

inpt = read_input(7, line_parser=parser)
assert order(inpt, n_workers=5, delay=60) == 1133

"""
Day 16
"""
from utils import read_input
from networkx import Graph, shortest_path_length
from itertools import combinations


def search(dists, rates, path, flow):
    if len(flow) == 30:
        return path, flow, sum(flow)

    # handle base case of first node
    curr_flow = flow[-1] if flow else 0
    # new flow with node turned on
    new_flow = curr_flow + rates[path[-1]]

    options = []
    for (i, j), d in dists.items():
        # not one of the connected edges
        if path[-1] != i:
            continue
        # if already in path skip
        if j in path:
            continue
        # if move will cause longer path longer than 30
        if (len(flow) + d) > 30:
            continue
        options.append(
            search(
                dists,
                rates,
                path + [j],
                flow + ([new_flow] * d),
            )
        )

    # if no options work wait it out at current node
    if len(options) == 0:
        flow = flow + ([new_flow] * (30 - len(flow)))
        return path, flow, sum(flow)

    return max(options, key=lambda x: x[2])


def optimize_flow(valves):
    G = Graph()
    flow_nodes = ["AA"]
    rates = {"AA": 0}
    # setup the graph
    for v, r, e in valves:
        G.add_node(v)
        for edge in e:
            G.add_edge(v, edge)
        if r != 0:
            flow_nodes.append(v)
            rates[v] = r

    # get all the distances between flow nodes
    dists = {}
    for i, j in combinations(flow_nodes, 2):
        d = shortest_path_length(G, i, j)
        dists[(i, j)] = d + 1
        dists[(j, i)] = d + 1

    ret = search(dists, rates, ["AA"], [])

    return ret[2]


test_inpt = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""


def parser(line):
    line = line.split()
    valve = line[1]
    rate = int([l.strip(";") for l in line if "=" in l][0].split("=")[1])
    edges = []
    for i, l in enumerate(line):
        if l in ["valves", "valve"]:
            edges = [l.strip(",") for l in line[i + 1 :]]
            break
    return valve, rate, edges


test_valves = [parser(line) for line in test_inpt.split("\n")]

assert optimize_flow(test_valves) == 1651


valves = read_input(16, line_parser=parser)
path_count = 0
assert optimize_flow(valves) == 1871

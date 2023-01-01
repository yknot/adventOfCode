"""
Day 16
"""
from utils import read_input
from networkx import Graph, shortest_path_length
from itertools import combinations
from collections import defaultdict


def search(dists, rates, edges, path_a, path_b, flow_a, flow_b):
    if len(flow_a) == 26:
        return path_a, path_b, flow_a, flow_b, sum(flow_a) + sum(flow_b)

    # handle base case of first node
    curr_flow_a = flow_a[-1] if flow_a else 0
    curr_flow_b = flow_b[-1] if flow_b else 0
    # new flow with node turned on
    new_flow_a = curr_flow_a + rates[path_a[-1]]
    new_flow_b = curr_flow_b + rates[path_b[-1]]

    options = []
    for j_a in edges[path_a[-1]]:
        # if already in path skip
        if j_a in path_a or j_a in path_b:
            continue
        d_a = dists[(path_a[-1], j_a)]
        # if move will cause longer path longer than 26
        if (len(flow_a) + d_a) > 26:
            continue

        for j_b in edges[path_b[-1]]:
            # if already in path skip
            if j_b == j_a or j_b in path_a or j_b in path_b:
                continue
            d_b = dists[(path_b[-1], j_b)]
            # if move will cause longer path longer than 26
            if (len(flow_b) + d_b) > 26:
                continue

            options.append(
                search(
                    dists,
                    rates,
                    edges,
                    path_a + [j_a],
                    path_b + [j_b],
                    flow_a + ([new_flow_a] * d_a),
                    flow_b + ([new_flow_b] * d_b),
                )
            )

        options.append(
            search(
                dists,
                rates,
                edges,
                path_a + [j_a],
                path_b,
                flow_a + ([new_flow_a] * d_a),
                flow_b + ([new_flow_b] * (26 - len(flow_b))),
            )
        )

    # if no options work wait it out at current node
    if len(options) == 0:
        for j_b in edges[path_b[-1]]:
            # if already in path skip
            if j_b in path_a or j_b in path_b:
                continue
            d_b = dists[(path_b[-1], j_b)]
            # if move will cause longer path longer than 26
            if (len(flow_b) + d_b) > 26:
                continue

            options.append(
                search(
                    dists,
                    rates,
                    edges,
                    path_a,
                    path_b + [j_b],
                    flow_a + ([new_flow_a] * (26 - len(flow_a))),
                    flow_b + ([new_flow_b] * d_b),
                )
            )

        if len(options) == 0:
            flow_a = flow_a + ([new_flow_a] * (26 - len(flow_a)))
            flow_b = flow_b + ([new_flow_b] * (26 - len(flow_b)))
            return path_a, path_b, flow_a, flow_b, sum(flow_a) + sum(flow_b)

    return max(options, key=lambda x: x[-1])


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
    edges = defaultdict(list)
    for i, j in combinations(flow_nodes, 2):
        d = shortest_path_length(G, i, j)
        dists[(i, j)] = d + 1
        edges[i].append(j)
        dists[(j, i)] = d + 1
        edges[j].append(i)

    ret = search(dists, rates, edges, ["AA"], ["AA"], [], [])

    return ret[-1]


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

assert optimize_flow(test_valves) == 1707

valves = read_input(16, line_parser=parser)

assert optimize_flow(valves) == 2416

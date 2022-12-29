"""
Day 16
"""
from utils import read_input
from dataclasses import dataclass


@dataclass
class Valve:
    name: str
    rate: int
    edges: list[str]


path_count = 0


def search(valves, path, curr_v, on, flow):
    global path_count
    if len(path) == 30:
        path_count += 1
        # print(path, flow, sum(flow))
        print(path)
        if path_count == 1000:
            import sys

            sys.exit(1)
        return path, flow, sum(flow)
    if len(on) == len(valves):
        return search(valves, path + ["noop"], curr_v, on, flow + [flow[-1]])

    curr_flow = flow[-1]

    options = []

    if curr_v not in on:
        new_flow = curr_flow + valves[curr_v].rate
        ret = search(
            valves,
            path + [curr_v + "_on"],
            curr_v,
            on + [curr_v],
            flow + [new_flow],
        )
        options.append(ret)

    for edge in valves[curr_v].edges:
        # don't go back to the previous node
        if len(path) >= 2 and edge == path[-2]:
            continue
        ret = search(
            valves,
            path + [edge],
            edge,
            on,
            flow + [curr_flow],
        )
        options.append(ret)

    if len(options) == 0:
        return [], [], 0
    return max(options, key=lambda x: x[2])


def optimize_flow(valves):
    valves = {v.name: v for v in valves}

    ret = search(valves, ["AA"], "AA", [v for v in valves if valves[v].rate == 0], [0])
    print(ret[0])
    print(ret[1])
    print(ret[2])
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
    return Valve(valve, rate, edges)


test_valves = [parser(line) for line in test_inpt.split("\n")]

assert optimize_flow(test_valves) == 1651
print(path_count)

valves = read_input(16, line_parser=parser)

# assert optimize_flow(valves) == 1871

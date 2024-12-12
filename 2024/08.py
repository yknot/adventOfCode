from collections import defaultdict
from itertools import combinations


example = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""


def parse_input(data):
    nodes = defaultdict(list)
    height = len(data.split())
    width = len(data.split()[0])

    for i, line in enumerate(data.split()):
        for j, val in enumerate(line):
            if val != ".":
                nodes[val].append((i, j))

    return nodes, height, width


def print_grid(nodes, height, width, antinodes):
    for i in range(height):
        row = []
        for j in range(width):
            found = False
            for node, locs in nodes.items():
                if (i, j) in locs:
                    row.append(node)
                    found = True
                    break
            if found:
                continue
            elif (i, j) in antinodes:
                row.append("#")
            else:
                row.append(".")

        print("".join(row))
    print()


def compute_antinodes(data, resonant=False):
    nodes, height, width = parse_input(data)

    antinodes = set()
    for _, locs in nodes.items():
        if len(locs) < 2:
            continue

        for (x_i, x_j), (y_i, y_j) in combinations(locs, 2):
            dist_i = y_i - x_i
            dist_j = y_j - x_j

            pt_1 = (x_i - dist_i, x_j - dist_j)
            if 0 <= pt_1[0] < height and 0 <= pt_1[1] < width:
                antinodes.add(pt_1)
                if resonant:
                    while True:
                        pt_1 = (pt_1[0] - dist_i, pt_1[1] - dist_j)
                        if 0 <= pt_1[0] < height and 0 <= pt_1[1] < width:
                            antinodes.add(pt_1)
                        else:
                            break

            pt_2 = (y_i + dist_i, y_j + dist_j)
            if 0 <= pt_2[0] < height and 0 <= pt_2[1] < width:
                antinodes.add(pt_2)
                if resonant:
                    while True:
                        pt_2 = (pt_2[0] + dist_i, pt_2[1] + dist_j)
                        if 0 <= pt_2[0] < height and 0 <= pt_2[1] < width:
                            antinodes.add(pt_2)
                        else:
                            break

    # print_grid(nodes, height, width, antinodes)
    result = len(antinodes)
    if resonant:
        all_vals = set()
        for vals in nodes.values():
            all_vals = all_vals.union(vals)

        result = len(antinodes.union(all_vals))
    return result


res = compute_antinodes(example)
assert res == 14, res

with open("08_input") as f:
    res = compute_antinodes(f.read())
    assert res == 359, res


res = compute_antinodes(example, resonant=True)
assert res == 34, res

with open("08_input") as f:
    res = compute_antinodes(f.read(), resonant=True)
    assert res == 1293, res

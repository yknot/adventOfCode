"""
Day 19
"""
from itertools import permutations
from utils import read_input
from IPython import embed

transformations = [
    # z is up
    lambda x, y, z: (x, y, z),  # normal
    lambda x, y, z: (y, -1 * x, z),  # 90 right
    lambda x, y, z: (-1 * x, -1 * y, z),  # 180 right
    lambda x, y, z: (-1 * y, x, z),  # 270 right
    # z is down
    lambda x, y, z: (y, x, -1 * z),  # normal
    lambda x, y, z: (x, -1 * y, -1 * z),  # 90 right
    lambda x, y, z: (-1 * y, -1 * x, -1 * z),  # 180 right
    lambda x, y, z: (-1 * x, y, -1 * z),  # 270 right
    # z is right (x)
    lambda x, y, z: (z, y, -1 * x),
    lambda x, y, z: (z, -1 * x, -1 * y),
    lambda x, y, z: (z, -1 * y, x),
    lambda x, y, z: (z, x, y),
    # z is left (-1 * x)
    lambda x, y, z: (-1 * z, y, x),
    lambda x, y, z: (-1 * z, -1 * x, y),
    lambda x, y, z: (-1 * z, -1 * y, -1 * x),
    lambda x, y, z: (-1 * z, x, -1 * y),
    # z is forward (y)
    lambda x, y, z: (x, z, -1 * y),
    lambda x, y, z: (y, z, x),
    lambda x, y, z: (-1 * x, z, y),
    lambda x, y, z: (-1 * y, z, -1 * x),
    # z is backward (-1 * y)
    lambda x, y, z: (x, -1 * z, y),
    lambda x, y, z: (y, -1 * z, -1 * x),
    lambda x, y, z: (-1 * x, -1 * z, -1 * y),
    lambda x, y, z: (-1 * y, -1 * z, x),
]


def calc_dist(pt1, pt2, sum_flag=False):
    if sum_flag:
        return (pt1[0] + pt2[0]), (pt1[1] + pt2[1]), (pt1[2] + pt2[2])
    return (pt1[0] - pt2[0]), (pt1[1] - pt2[1]), (pt1[2] - pt2[2])


def flatten(lst):
    new_lst = []
    for x, y in lst:
        new_lst.append(x)
        new_lst.append(y)

    return new_lst


def prep_scanners(inpt):
    scanners = {}
    # parse input data into dictionary of int keys and list values
    #   each value in the list being length of three and ints
    current_scanner = None
    for line in inpt:
        if type(line) == int:
            scanners[line] = []
            current_scanner = line
        if type(line) == list:
            scanners[current_scanner].append(tuple(line))

    return scanners


def calc_scanners_dist(scanner, t=None):
    # get all the distances between points across scanners
    scanner_distances = {}
    for pt1, pt2 in permutations(scanner, 2):
        if t:
            scanner_distances[calc_dist(t(*pt1), t(*pt2))] = [
                t(*pt1),
                t(*pt2),
            ]
        else:
            scanner_distances[calc_dist(pt1, pt2)] = [pt1, pt2]

    return scanner_distances


def find_mappings(scanner_dists, scanner_dists_t):
    mappings, scanner_coords = [], {}

    for x in scanner_dists.keys():
        y_opts = list(scanner_dists.keys())
        y_opts.remove(x)
        dists = set(scanner_dists[x])

        # for all possible y values
        for y in y_opts:
            # try each transformation
            for i in range(len(transformations)):
                dists_t = set(scanner_dists_t[y][i])
                intersect = dists.intersection(dists_t)
                # if an intersection
                if intersect:
                    x_pts = set(flatten([scanner_dists[x][it] for it in intersect]))
                    # if the intersection is large enough
                    if len(x_pts) >= 12:
                        y_pts = set(
                            flatten([scanner_dists_t[y][i][it] for it in intersect])
                        )
                        # if they all overlap
                        if len(y_pts) >= 12:
                            # print(x, y)
                            mappings.append([(x, y), i])
                            it = list(intersect)[0]
                            pt1_x, pt2_x = scanner_dists[x][it]
                            pt1_y, pt2_y = scanner_dists_t[y][i][it]
                            pos_guess_1 = calc_dist(pt1_x, pt1_y)
                            pos_guess_2 = calc_dist(pt2_x, pt2_y)
                            if pos_guess_1 == pos_guess_2:
                                scanner_coords[(x, y)] = pos_guess_1

                            break

    return mappings, scanner_coords


def find_pos(mappings, scanner_coords, cur_x, visited):
    print(f"looking for {cur_x}")

    for (x, y), t in mappings:
        if x == cur_x and y not in visited:
            visited.append(y)
            scanner_pos = find_pos(mappings, scanner_coords, y, visited)
            print(x, y)
            pos = scanner_coords[(x, y)]
            # where t is for right coord mapping,
            # calc_dist(tranformations[t])
            # print(
            #     calc_dist(
            #         transformations[t](*pos]), scanner_coords, sum_flag=True
            #     )
            # )

    return scanner_pos


"""
In [16]: calc_dist(transformations[t](*scanner_coords[(1, 4)]), scanner_coords[(0, 1)], sum_flag=Tru
    ...: e)
Out[16]: (-20, -1133, 1061)

In [17]: calc_dist(transformations[t](*scanner_coords[(1, 3)]), scanner_coords[(0, 1)], sum_flag=Tru
    ...: e)
Out[17]: (-92, -2380, -20)"""


def count_beacons(inpt):
    # dictionary of keys scanner ids and coordinates
    scanners = prep_scanners(inpt)
    # dictionary of keys distance and values the two points
    scanner_dists = {}
    scanner_dists_t = {}
    for k, v in scanners.items():
        scanner_dists[k] = calc_scanners_dist(v)
        scanner_dists_t[k] = {}
        for i, t in enumerate(transformations):
            scanner_dists_t[k][i] = calc_scanners_dist(v, t=t)

    # for pairs of scanners the x scanner remains constant
    # and the y scanner tests different transformations
    mappings, scanner_coords = find_mappings(scanner_dists, scanner_dists_t)

    embed()

    scanner_pos = find_pos(mappings, scanner_coords, 0, [0])


def parser(line):
    if "---" in line:
        return int(line.strip("- \n").split()[1])
    if "," in line:
        return [int(l) for l in line.split(",")]


test_inpt = list(read_input(19, line_parser=parser, file_template="{:02}_test_input"))
assert count_beacons(test_inpt) == 3621

inpt = read_input(19, line_parser=parser)
res = count_beacons(inpt)
assert res == 403

from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations
from math import sqrt

example = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""


@dataclass(frozen=True)
class Junction:
    x: int
    y: int
    z: int


def distance(first: Junction, second: Junction) -> float:
    return sqrt(
        (first.x - second.x) ** 2
        + (first.y - second.y) ** 2
        + (first.z - second.z) ** 2
    )


def parse(inpt: str) -> list[Junction]:
    junctions = []
    for line in inpt.splitlines():
        x, y, z = line.split(",")
        junctions.append(Junction(int(x), int(y), int(z)))

    return junctions


def compute_distances(
    junctions: list[Junction],
) -> list[tuple[Junction, Junction, float]]:
    dists = []
    for a, b in combinations(junctions, 2):
        dists.append((a, b, distance(a, b)))

    return sorted(dists, key=lambda item: item[2])


def count_connections(inpt: str, count: int | None = None) -> int:
    junctions = parse(inpt)

    # find straight line distance between all junctions and sort
    dists = compute_distances(junctions)
    if count:
        dists = dists[:count]

    # combine the pairs of the lowest `count` distances into circuits
    seen = {}
    idx = 0
    for first, second, _ in dists:
        # if they have already both been seen
        if first in seen and second in seen:
            # and they are in different groups
            if seen[first] != seen[second]:
                first_group = seen[first]
                second_group = seen[second]
                # combine the groups
                for junction, circuit in seen.items():
                    if circuit == second_group:
                        seen[junction] = first_group

        # if we've already seen one add it to the same circuit
        elif first in seen:
            seen[second] = seen[first]
        elif second in seen:
            seen[first] = seen[second]
        # if they are both new make a new circuit
        else:
            seen[first] = idx
            seen[second] = idx
            idx += 1

        # part 2 when we are looking for one fully connected circuit
        if len(seen) == len(junctions) and list(seen.values()).count(
            seen[first]
        ) == len(seen):
            return first.x * second.x

    # compute sizes of circuits
    circuit_sizes = defaultdict(int)
    for val in seen.values():
        circuit_sizes[val] += 1

    # find top 3 circuits
    a, b, c = sorted(circuit_sizes.values(), reverse=True)[:3]

    return a * b * c


with open("08_input") as f:
    data = f.read()

assert count_connections(example, count=10) == 40
assert count_connections(data, count=1000) == 133574

assert count_connections(example) == 25272
assert count_connections(data) == 2435100380

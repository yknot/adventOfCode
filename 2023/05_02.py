"""
Day 5
"""
from utils import read_input

test_inpt = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


def convert(lines):
    mapping = {}
    data = {}
    to, fro = "", ""
    maps = []
    for line in lines:
        if ":" in line:
            if line.startswith("seeds:"):
                data["seed"] = [int(l) for l in line.split()[1:]]
                continue
            to, fro = line.split()[0].split("-to-")
        elif line:
            maps.append([int(l) for l in line.split()])
        else:
            if to:
                mapping[to] = fro
                data[fro] = maps
                maps = []
    mapping[to] = fro
    data[fro] = maps

    min_loc = None
    idx = 0
    while idx < len(data["seed"]):
        for seed in range(data["seed"][idx], data["seed"][idx] + data["seed"][idx + 1]):
            val = seed
            to = "seed"
            fro = mapping[to]
            while to != "location":
                for dest, source, rng in data[fro]:
                    if source <= val < (source + rng):
                        val = dest + (val - source)
                        break
                to = fro
                if to == "location":
                    break
                fro = mapping[to]
            if not min_loc:
                min_loc = val
            elif val < min_loc:
                min_loc = val
        idx += 2

    return min_loc


inpt = list(read_input(5))

assert convert(test_inpt.split("\n")) == 46

print(convert(inpt))

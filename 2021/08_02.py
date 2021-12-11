"""
Day 8, part 2
"""
from utils import read_input


def decode_line(line):
    front, back = line
    front = sorted(front, key=len)
    mapping = {}
    # get obvious
    mapping[1] = set(front[0])  # 1 is len 2
    mapping[7] = set(front[1])  # 7 is len 3
    mapping[4] = set(front[2])  # 4 is len 4
    mapping[8] = set(front[-1])  # 8 is len 7
    # get len 6 nums
    for f in front[6:9]:
        f = set(f)
        # 6 doesn't have both from 1
        if mapping[1] - f:
            mapping[6] = f
        # 0 doesn't have all from 4
        elif mapping[4] - f:
            mapping[0] = f
        else:
            mapping[9] = f

    # get len 5 nums
    for f in front[3:6]:
        f = set(f)
        # 5 is only one off of 6
        if len(mapping[6] - f) == 1:
            mapping[5] = f
        # 2 doesn't have one of the values from 1
        elif mapping[1] - f:
            mapping[2] = f
        else:
            mapping[3] = f

    val = []
    for b in back:
        b = set(b)
        for m, v in mapping.items():
            if b == v:
                val.append(m)
                break

    return int("".join([str(i) for i in val]))


def find_outputs(inpt):
    tot = 0
    for line in inpt:
        tot += decode_line(line)

    return tot


def parser(inpt):
    decode, result = inpt.strip().split(" | ")
    return [decode.split(), result.split()]


small_test = parser(
    "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
)
assert find_outputs([small_test]) == 5353

test_inpt = list(read_input(8, line_parser=parser, file_template="{:02}_test_input"))
assert find_outputs(test_inpt) == 61229

inpt = list(read_input(8, line_parser=parser))
assert find_outputs(inpt) == 1028926

"""
Day 6
"""
from utils import read_input

test_inpt = [
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
    "bvwbjplbgvbhsrlpgdmjqwftvncz",
    "nppdvjthqldpwncqszvftbrmjlhg",
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
]


def get_marker(inpt):
    i = 14
    while i < len(inpt):
        if len(set(inpt[i - 14 : i])) == 14:
            break
        i += 1

    return i


inpt = read_input(6)

output = [19, 23, 23, 29, 26]
for i, t in enumerate(test_inpt):
    assert get_marker(t) == output[i]


assert get_marker(inpt) == 3588

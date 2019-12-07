"""
Day 4

facts about password
- 6 digit number
- value is within puzzle input
- two adjacent digits are the same
    - e.g. 22 in 122345
- going from left to right the digits never decrease

"""


def find_pwd(low, high):
    count = 0
    i = low
    while i < high:
        tmp_str = str(i)
        # dummy check to skip hundreds of values
        for j in range(5):
            if int(tmp_str[j]) > int(tmp_str[j + 1]):
                i = int(tmp_str[:j] + (tmp_str[j] * (6 - j)))
                break
        if str(i) != tmp_str:
            continue

        # check if two adjacent numbers
        if not any([1 if a == b else 0 for a, b in zip(tmp_str, tmp_str[1:])]):
            i += 1
            continue

        # check if increasing
        if any([1 if int(a) > int(b) else 0 for a, b in zip(tmp_str, tmp_str[1:])]):
            i += 1
            continue

        count += 1
        i += 1

    return count


puz_input = "353096-843212"

assert find_pwd(*[int(p) for p in puz_input.split("-")]) == 579

"""
Day 4 part 2

facts about password
- 6 digit number
- value is within puzzle input
- two adjacent digits are the same
    - e.g. 22 in 122345
    - only part of a pair not triple
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
        rep_count = 1
        rep = tmp_str[0]
        found = False
        for s in tmp_str[1:]:
            # if a match increment
            if rep == s:
                rep_count += 1
                continue
            # this means it didn't match and if the count is 2 we found a double
            elif rep_count == 2:
                found = True
                break
            # if not a double start checking next number
            rep_count = 1
            rep = s

        # double at the end of the string
        if rep_count == 2:
            found = True
        # if we didn't find a double move to the next iteration
        if not found:
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

assert find_pwd(*[int(p) for p in puz_input.split("-")]) == 358

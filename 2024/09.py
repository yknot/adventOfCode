example = "2333133121414131402"


def parse_data(data):
    uncompressed = []
    is_file = True
    file_id = 0
    for d in data:
        if is_file:
            for _ in range(int(d)):
                uncompressed.append(str(file_id))
            is_file = False
            file_id += 1
        else:
            for _ in range(int(d)):
                uncompressed.append(".")
            is_file = True

    return uncompressed


def reformat_data_quick(uncompressed):
    empty_idx = 0
    while uncompressed[empty_idx] != ".":
        empty_idx += 1

    idx = len(uncompressed) - 1
    while empty_idx < idx:
        if uncompressed[idx] != ".":
            uncompressed[empty_idx] = uncompressed[idx]
            uncompressed[idx] = "."
        while empty_idx < len(uncompressed) and uncompressed[empty_idx] != ".":
            empty_idx += 1

        if empty_idx >= len(uncompressed):
            break

        idx -= 1

    return uncompressed


def find_free(lst, length, limit):
    idx = lst.index(".")
    count = 0
    while idx < limit:
        if count == length:
            return idx - length
        if lst[idx] == ".":
            count += 1
        else:
            count = 0

        idx += 1


def reformat_data_full_files(data, uncompressed):
    orig_len = len(uncompressed)
    idx = len(uncompressed) - 1
    val = None
    seen = []
    while idx >= 0:
        if uncompressed[idx] != ".":
            # make sure we haven't moved it before
            if uncompressed[idx] in seen:
                idx -= 1
                continue
            seen.append(uncompressed[idx])

            # find out length of file
            val = uncompressed[idx]
            length = 1
            idx -= 1
            while uncompressed[idx] == val:
                idx -= 1
                length += 1
            idx += 1

            # swap out files if found
            empty_idx = find_free(uncompressed, length, idx)
            if empty_idx:
                uncompressed[empty_idx : empty_idx + length] = [val] * length
                uncompressed[idx : idx + length] = ["."] * length
            else:
                print(f"Couldn't find fit for {val} with length {length}")

        idx -= 1
    with open("uncompressed", "w") as f:
        f.write(str(uncompressed))

    seen = [int(i) for i in seen]
    assert seen == sorted(seen, reverse=True)
    assert len(seen) == len(data[::2])
    assert len(uncompressed) == orig_len

    for i, val in enumerate(data[::2]):
        assert uncompressed.count(str(i)) == int(val)

    return uncompressed


def checksum(uncompressed):
    total = 0
    for i, val in enumerate(uncompressed):
        if val == ".":
            continue
        total += i * int(val)

    return total


def calc_checksum(data, full_files=False):
    uncompressed = parse_data(data)
    if full_files:
        uncompressed = reformat_data_full_files(data, uncompressed)
    else:
        with open("uncompressed_start", "w") as f:
            f.write(str(uncompressed))
        uncompressed = reformat_data_quick(uncompressed)

    total = checksum(uncompressed)
    return total


res = calc_checksum(example)
assert res == 1928, res


with open("09_input") as f:
    res = calc_checksum(f.read())
    assert res == 6421128769094, res

res = calc_checksum(example, full_files=True)
assert res == 2858, res


with open("09_input") as f:
    res = calc_checksum(f.read(), full_files=True)
    assert res == 6421128769094, res

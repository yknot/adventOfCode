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


def find_free(lst: list, length: int, limit: int) -> int:
    idx = lst.index(".")
    count = 0
    while idx <= limit:
        if count == length:
            return idx - length
        if lst[idx] == ".":
            count += 1
        else:
            count = 0

        idx += 1

    return -1


def reformat_data_full_files(data, uncompressed):
    orig_count = uncompressed.count(".")
    orig_len = len(uncompressed)
    len_ids = len(data[::2])
    for i, length in enumerate(data[::2][::-1]):
        length = int(length)
        val = str(len_ids - 1 - i)
        idx = uncompressed.index(val)
        assert uncompressed[idx : idx + length] == [str(val)] * length

        empty_idx = find_free(uncompressed, length, idx)

        if empty_idx != -1:
            assert uncompressed[empty_idx : empty_idx + length] == ["."] * length

            uncompressed[empty_idx : empty_idx + length] = [val] * length
            uncompressed[idx : idx + length] = ["."] * length

    # tests
    assert len(uncompressed) == orig_len
    for i, val in enumerate(data[::2]):
        assert uncompressed.count(str(i)) == int(val)
        start = uncompressed.index(str(i))
        assert uncompressed[start : start + int(val)] == [str(i)] * int(val)
    assert uncompressed.count(".") == orig_count

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
    assert res == 6448168620520, res

from functools import reduce


def flip_data(arr, curr, l):
    """flip the data accounting for wrapping"""
    # base case
    if l == 1:
        return

    # get the subset
    subset = []
    for i in range(l):
        n = (curr + i) % len(arr)
        subset.append(arr[n])

    # reverse
    subset = subset[::-1]

    # put back
    for i in range(l):
        n = (curr + i) % len(arr)
        arr[n] = subset[i]


def chunks(l, n):
    """split l into chunks of size n"""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def sparse_hash(arr):
    """calculate sparse hash"""

    hash = ''
    # iterate on size 16 chunks
    for c in chunks(arr, 16):
        assert len(c) == 16
        # xor the chunk together
        res = reduce((lambda x, y: x ^ y), c)
        # convert to hex
        res = hex(res)[2:].zfill(2)
        # add to string
        hash += res

    return hash


def hash_data(input_str):
    """hash the data with knot tying"""
    lengths = convert_length(input_str)
    numbers = list(range(256))
    current = 0
    skip_size = 0
    # run 64 times
    for _ in range(64):
        for l in lengths:
            # get slice
            flip_data(numbers, current, l)

            # move current spot
            current = (current + l + skip_size) % len(numbers)
            # increase skip size
            skip_size += 1

    return sparse_hash(numbers)


def convert_length(lengths_raw):
    """convert from char to ascii codes"""
    return list(map(ord, lengths_raw)) + [17, 31, 73, 47, 23]


if __name__ == "__main__":
    # test input
    assert hash_data('') == 'a2582a3a0e66e6e86e3812dcb672a272'
    assert hash_data('AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'
    assert hash_data('1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d'
    assert hash_data('1,2,4') == '63960835bcdc130f0b66d7ff4f6a5a8e'

    print(hash_data("76,1,88,148,166,217,130,0,128,254,16,2,130,71,255,229"))

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


def hash_data(numbers, lengths):
    """hash the data with knot tying"""
    current = 0
    skip_size = 0
    for l in lengths:
        # get slice
        flip_data(numbers, current, l)

        # move current spot
        current = (current + l + skip_size) % len(numbers)
        # increase skip size
        skip_size += 1

    return numbers[0] * numbers[1]


# test input
numbers = list(range(5))
lengths = [3, 4, 1, 5]

assert hash_data(numbers, lengths) == 12
assert len(numbers) == 5
assert numbers == [3, 4, 2, 1, 0]
# real input
numbers = list(range(256))
lengths_raw = "76,1,88,148,166,217,130,0,128,254,16,2,130,71,255,229"
lengths = [int(i) for i in lengths_raw.split(',')]

print(hash_data(numbers, lengths))

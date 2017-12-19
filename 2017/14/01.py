from hash import hash_data


def defrag(input_str):
    """construct the defrag grid"""
    total = 0
    for i in range(128):
        h = hash_data(input_str + '-' + str(i))
        for val in h:
            total += sum([int(i) for i in bin(int(val, 16))[2:]])

    return total


assert defrag('flqrgnkx') == 8108
print(defrag('wenycdww'))

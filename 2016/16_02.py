def dragon(a):
    # make a copy
    b = list(a)
    # reverse the characters
    b.reverse()
    # replace all 0 with 1 and 1 with 0
    b = ['0' if i == '1' else '1' for i in b]
    # result is a + '0' + b 
    return a + '0' + ''.join(b)


def checksum(a):
    cs = ''
    i = 0
    while i < len(a):
        if a[i] == a[i + 1]:
            cs += '1'
        else:
            cs += '0'
        i += 2
    if len(cs) % 2 == 0:
        return checksum(cs)

    return cs


def fill_disk(disk, n):
    if len(disk) >= n:
        return checksum(disk[:n])

    return fill_disk(dragon(disk), n)


# tests
assert dragon('1') == '100'
assert dragon('0') == '001'
assert dragon('11111') == '11111000000'
assert dragon('111100001010') == '1111000010100101011110000'

assert checksum('110010110100') == '100'

assert fill_disk('10000', 20) == '01100'

print(fill_disk('01110110101001000', 35651584))

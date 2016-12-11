"""advent of code 2016 day 9 part 1"""



def decompress(d):
    final = ''
    i = 0
    while i < len(d):
        if d[i] == '(':
            i += 1
            cmd = ''
            # capture command in ( )
            while d[i] != ')':
                cmd += d[i]
                i += 1
            cmd = [int(c) for c in cmd.split('x')]

            # get repeated section
            i += 1
            repeat = ''
            for _ in range(cmd[0]):
                repeat += d[i]
                i += 1

            # add repeated section
            for _ in range(cmd[1]):
                final += repeat

        else:
            final += d[i]
            i += 1

    return final


assert decompress('ADVENT') == 'ADVENT'
assert decompress('A(1x5)BC') == 'ABBBBBC'
assert decompress('(3x3)XYZ') == 'XYZXYZXYZ'
assert decompress('A(2x2)BCD(2x2)EFG') == 'ABCBCDEFEFG'
assert decompress('(6x1)(1x3)A') == '(1x3)A'
assert decompress('X(8x2)(3x3)ABCY') == 'X(3x3)ABC(3x3)ABCY'

data = open('input').read()

print(len(decompress(data)))
    

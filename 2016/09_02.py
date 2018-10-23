"""advent of code 2016 day 9 part 2"""



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

            repeat = decompress(repeat)
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
assert decompress('X(8x2)(3x3)ABCY') == 'XABCABCABCABCABCABCY'
assert len(decompress('(27x12)(20x12)(13x14)(7x10)(1x12)A')) == 241920
assert len(decompress('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN')) == 445

data = open('input').read()

print(len(decompress(data)))
    

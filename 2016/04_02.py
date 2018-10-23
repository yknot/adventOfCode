"""day 4 of advent of code 2016 part 2"""
raw = open('input').read().splitlines()
# raw = ['a-b-c-d-e-f-g-h-987[abcde]']
# lines = [''.join(r.split('-')) for r in raw]
lines = [l.strip(']').split('[') for l in raw]

start = ord('a')

for l in lines:
    sector_id = int(''.join([c for c in l[0] if c.isnumeric()]))
    chars = ''.join([c for c in l[0] if c.isalpha() or c == '-'])
    decrypt = ''
    for c in chars:
        if c != '-':
            new_c = chr((((ord(c) - start) + sector_id) % 26) + start)
        else:
            new_c = c
        decrypt = decrypt + new_c            

    if decrypt.find('north') != -1:
        print(decrypt)
        print(sector_id)


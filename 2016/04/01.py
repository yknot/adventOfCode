"""day 4 of advent of code 2016 part 1"""
raw = open('input').read().splitlines()
# raw = ['a-b-c-d-e-f-g-h-987[abcde]']
lines = [''.join(r.split('-')) for r in raw]
lines = [l.strip(']').split('[') for l in lines]

total = 0
for l in lines:
    sector_id = int(''.join([c for c in l[0] if c.isnumeric()]))
    chars = ''.join([c for c in l[0] if c.isalpha()])
    counts = {}
    for c in chars:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    check_sum = ''
    while len(check_sum) < 5:
        possible = [k for k, v in counts.items() if v == max(counts.values())]
        check_sum = check_sum + ''.join(sorted(possible))[:5 - len(check_sum)]
        counts = {k: v for k, v in counts.items() if v != max(counts.values())}

    if check_sum == l[1]:
        total += sector_id


print(total)

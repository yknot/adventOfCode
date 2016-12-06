"""advent of code 2016 day 6 part 2"""
data = open('input').read().splitlines()
# data = ['eedadn',
#         'drvtee',
#         'eandsr',
#         'raavrd',
#         'atevrs',
#         'tsrnev',
#         'sdttsa',
#         'rasrtv',
#         'nssdts',
#         'ntnada',
#         'svetve',
#         'tesnvt',
#         'vntsnd',
#         'vrdear',
#         'dvrsen',
#         'enarar']

length = len(data[0])
final = ''
for i in range(length):
    counts = {}
    for d in data:
        if d[i] in counts:
            counts[d[i]] += 1
        else:
            counts[d[i]] = 1

    final += {v: k for k, v in counts.items()}[min(counts.values())]

print(final)
